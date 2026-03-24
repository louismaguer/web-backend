---
short_title: "DB 2/2: relationships"
---

# DB 2/2: relationships between tables

So far, our database contained a **single table** (`users`); however  
real applications almost always involve **multiple tables that are related to each other** !

Examples:

- a user can have **many posts**,
- a post belongs to **one user**,
- a course has **many students**, and
- a student can attend **many courses**.

This is where **relationships between tables** come into play.

---

## Why relationships matter

Without relationships, all data would live in a single table, leading to:

- duplicated information,
- inconsistencies (same data repeated in multiple places),
- poor scalability.

Relational databases solve this by **splitting data into multiple tables** and linking them together using **foreign keys**.

A foreign key is simply a column that references the **primary key of another table**.

---

## One-to-many relationships

The most common relationship is **one-to-many**.

Example:  
👉 One `User` can have many `Post`s, but each `Post` belongs to exactly one `User`.

See also the complete code in `python/db-relationships/user_posts.py`.

---

## Database view

Conceptually, this looks like:

- `users` table  
  - `id` (primary key) 
  - ... details like `name`, `email`, etc
- `posts` table  
  - `id` (primary key) 
  - ... details like `title`, `content`, etc
  - **`user_id`** (foreign key → `users.id`)

The `user_id` column is what links a post to its author.

---

## Defining a relationship in SQLModel

With SQLModel, we explicitly describe both:

1. the **foreign key column**, and  
2. the **Python relationship**.

```{code} python
:class: smaller
:linenos:
:emphasize-lines: 7,15-16

from sqlmodel import SQLModel, Field, Relationship

class User(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    name: str

    posts: list["Post"] = Relationship(back_populates="user")


class Post(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    title: str
    content: str

    user_id: int = Field(foreign_key="user.id")
    user: User = Relationship(back_populates="posts")
```

Key ideas:

- `user_id` is the **foreign key** stored in the database.
- `posts` and `user` are **Python attributes**, not database columns.
- `back_populates` keeps both sides of the relationship in sync.

This allows you to navigate relationships naturally in Python:

```python
post.user.name
user.posts
```

---

## Many-to-one vs one-to-many

Note that:

- **one-to-many** and **many-to-one** are two sides of the same relationship.

In our example:

- from `User` → `Post`: one-to-many,
- from `Post` → `User`: many-to-one.

SQLModel (and SQLAlchemy) require you to define **both sides explicitly** if you want bidirectional access.

---

## Many-to-many relationships

Some relationships are **many-to-many**.

Example:  
👉 A student can attend many courses, and a course can have many students.

Relational databases handle this using an **association table** (also called a junction table).

See the code in `python/db-relationships/students_courses.py` for a complete example.

---

## Association table concept

Instead of linking `students` directly to `courses`, we introduce a third table:

- `students`
- `courses`
- **`enrollments`**
  - **`student_id`**
  - **`course_id`**

Each row in **`enrollments`** represents **one association** (one student in one course).

---

## SQLModel approach

In SQLModel, the association table is usually modeled explicitly:

```{code} python
:linenos:
:emphasize-lines: 2-3
class Enrollment(SQLModel, table=True):
    student_id: int = Field(foreign_key="student.id", primary_key=True)
    course_id: int = Field(foreign_key="course.id", primary_key=True)
```

Then referenced from both sides:

```{code} python
:linenos:
:emphasize-lines: 5-8,15-18
class Student(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    name: str

    courses: list["Course"] = Relationship(
        back_populates="students",
        link_model=Enrollment
    )


class Course(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    title: str

    students: list[Student] = Relationship(
        back_populates="courses",
        link_model=Enrollment
    )
```

This may look verbose, but it gives you:

- full control over the relationship,
- the ability to add extra fields to the association table later (e.g. grade, enrollment date).

---

## Loading related data

By default, relationships are **lazy-loaded**:

- related objects are fetched from the database **only when accessed**.

This is efficient, but it has consequences in APIs:

- returning related objects directly may trigger extra (join) queries,
- plus, circular references can appear when serializing.

In practice, APIs often:

- use **response models** (Pydantic schemas),
- to control exactly which related fields are included,
- and avoid returning deeply nested objects by default.

---

## Relationships and API design

Relationships strongly influence how you design your API:

- Should `/users/1` include the user’s posts ?
- Should `/posts/` include the full user object or just `user_id` ?
- Do you want nested creation (create user + posts in one request) ?

There is no single correct answer — it depends on:

- performance,
- clarity of the API,
- how clients consume the data.

A common rule of thumb:

> Store relationships in the database,  
> but expose them **explicitly and deliberately** in the API.

---

## Key takeaways

- Relationships link tables using **foreign keys**.
- SQLModel lets you describe relationships using **type hints** and `Relationship`.
- One-to-many is the most common pattern.
- Many-to-many requires an **association table**.
- Database relationships do not automatically imply API nesting.

Understanding relationships is a major step toward building **real-world data models** — and SQLModel makes this step far less painful than traditional ORMs.
