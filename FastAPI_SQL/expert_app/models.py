from sqlalchemy import Column, Integer, String, Float, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from database import Base

class Student(Base):
    __tablename__ = "students"

    id = Column(Integer, primary_key=True, index=True)
    firstname = Column(String)
    lastname = Column(String)
    average = Column(Float)
    graduated = Column(Boolean)
    courses = relationship("Course", back_populates="student")


class Course(Base):
    __tablename__ = "courses"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    unit = Column(Integer)
    student_id = Column(Integer, ForeignKey("students.id"))

    student = relationship("Student", back_populates="courses")
