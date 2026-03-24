### the models

from sqlmodel import SQLModel, Field, Relationship, select

class Enrollment(SQLModel, table=True):
    student_id: int = Field(foreign_key="student.id", primary_key=True)
    course_id: int = Field(foreign_key="course.id", primary_key=True)

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


### the endpoints

from fastapi import FastAPI, Depends, HTTPException
from sqlmodel import create_engine, Session

app = FastAPI()

# db boilerplate

db_url = "sqlite:///./students_courses.db"
engine = create_engine(db_url, echo=True)
SQLModel.metadata.create_all(engine)
def get_session():
    with Session(engine) as session:
        yield session


# creation endpoints

@app.post("/students/", response_model=Student)
def create_student(student: Student, session: Session = Depends(get_session)):
    session.add(student)
    session.commit()
    session.refresh(student)
    return student

@app.post("/courses/", response_model=Course)
def create_course(course: Course, session: Session = Depends(get_session)):
    session.add(course)
    session.commit()
    session.refresh(course)
    return course


# for example, an endpoint to mass-enroll students to a course

class CourseEnrollmentRequest(SQLModel):
    student_ids: list[int]

@app.post("/courses/{course_id}/students", response_model=Course)
def add_students_to_course(
    course_id: int,
    payload: CourseEnrollmentRequest,
    session: Session = Depends(get_session),
):
    course = session.get(Course, course_id)
    if not course:
        raise HTTPException(status_code=404, detail="Course not found")

    students = session.exec(
        select(Student).where(Student.id.in_(payload.student_ids))
    ).all()
    found_ids = {student.id for student in students}
    missing_ids = [sid for sid in payload.student_ids if sid not in found_ids]
    if missing_ids:
        raise HTTPException(
            status_code=404,
            detail=f"Students not found: {missing_ids}",
        )

    for student in students:
        if student not in course.students:  # avoid duplicate links
            course.students.append(student)

    session.add(course)
    session.commit()
    session.refresh(course)
    return course


# here we decide to expose courses with just their student IDs
class CourseRead(SQLModel):
    id: int
    title: str
    student_ids: list[int]

@app.get("/courses/{course_id}", response_model=CourseRead)
def get_course(course_id: int, session: Session = Depends(get_session)):
    course = session.get(Course, course_id)
    if not course:
        raise HTTPException(status_code=404, detail="Course not found")
    # fetch related students (eager loading)
    return CourseRead(
        id=course.id,
        title=course.title,
        student_ids=[student.id for student in course.students],
    )



"""
http :8000/students/ name="John Doe"
http :8000/students/ name="Jane Smith"
http :8000/courses/ title="Math 101"
http :8000/courses/1/students student_ids:='[1,2]'
http :8000/courses/1
"""
