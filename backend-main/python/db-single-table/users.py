from sqlmodel import SQLModel, Field

class User(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    name: str
    email: str
    is_active: bool = True


# typical boilerplate code

from sqlmodel import create_engine, Session

# local SQLite file
database_url = "sqlite:///./users.db"
engine = create_engine(database_url, echo=True)

# create tables
# of course this needs to come AFTER all model definitions...
SQLModel.metadata.create_all(engine)

# utility function to get a session
def get_session():
    with Session(engine) as session:
        yield session

# this uses so-called "dependency injection"
# meaning the session is (re-)created on demand by FastAPI

from fastapi import FastAPI, Depends

app = FastAPI()

@app.post("/users/", response_model=User)
def create_user(user: User, session: Session = Depends(get_session)):
    session.add(user)
    session.commit()
    session.refresh(user)  # reload the object with the generated ID
    return user

from typing import List

@app.get("/users/", response_model=List[User])
def list_users(session: Session = Depends(get_session)):
    users = session.query(User).all()
    return users
