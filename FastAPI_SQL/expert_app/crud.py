from sqlalchemy.orm import Session
from models import Student, Course

def create_student(db: Session, firstname: str, lastname: str, average: float, graduated: bool):
    student = Student(
        firstname=firstname,
        lastname=lastname,
        average=average,
        graduated=graduated
    )
    db.add(student)
    db.commit()
    db.refresh(student)
    return student

def create_course(db: Session, name: str, unit: int, student_id: int):
    course = Course(
        name=name,
        unit=unit,
        student_id=student_id
    )
    db.add(course)
    db.commit()
    db.refresh(course)
    return course

def get_students(db: Session):
    return db.query(Student).all()

def get_courses(db: Session):
    return db.query(Course).all()
