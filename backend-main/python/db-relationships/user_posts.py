### the models

from sqlmodel import SQLModel, Field, Relationship, select

class User(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    name: str

    posts: list["Post"] = Relationship(back_populates="user")

class Post(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    content: str

    user_id: int = Field(foreign_key="user.id")
    user: User = Relationship(back_populates="posts")


### the endpoints

from fastapi import FastAPI, Depends, HTTPException
from sqlmodel import create_engine, Session

app = FastAPI()

# db boilerplate

db_url = "sqlite:///./user_posts.db"
engine = create_engine(db_url, echo=True)
SQLModel.metadata.create_all(engine)
def get_session():
    with Session(engine) as session:
        yield session


# creation endpoints

@app.post("/users/", response_model=User)
def create_user(user: User, session: Session = Depends(get_session)):
    session.add(user)
    session.commit()
    session.refresh(user)
    return user

@app.post("/posts/", response_model=Post)
def create_post(post: Post, session: Session = Depends(get_session)):
    session.add(post)
    session.commit()
    session.refresh(post)
    return post


# retrieval endpoints
# here for example we expose 2 endpoints:
# - just list the user's basic info
# - same but with the user's posts included

@app.get("/users/{user_id}", response_model=User)
def get_user(user_id: int, session: Session = Depends(get_session)):
    user = session.get(User, user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user


# for the second one we need to define a custom model to include the posts
# here we decide to expose the full Post objects (not just their ids)
class UserWithPosts(SQLModel):
    id: int
    name: str
    posts: list[Post] = []

@app.get("/users/{user_id}/with-posts", response_model=UserWithPosts)
def get_user_with_posts(user_id: int, session: Session = Depends(get_session)):
    user = session.get(User, user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    posts = session.exec(select(Post).where(Post.user_id == user_id)).all()
    return UserWithPosts(
        id=user.id,
        name=user.name,
        posts=posts,
    )

"""
http :8000/users/ name="Alice"
http :8000/posts/ content="Hello world!" user_id:=1
http :8000/posts/ content="Another post" user_id:=1
http :8000/users/1
http :8000/users/1/with-posts
"""
