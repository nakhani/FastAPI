from fastapi import FastAPI, Depends
from database import engine, Base, SessionLocal
from crud import create_student, create_course, get_students, get_courses
from sqlalchemy.orm import Session

app = FastAPI()

Base.metadata.create_all(bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/students/")
def add_student(firstname: str, lastname: str, average: float, graduated: bool, db: Session = Depends(get_db)):
    return create_student(db, firstname, lastname, average, graduated)

@app.post("/courses/")
def add_course(name: str, unit: int, student_id: int, db: Session = Depends(get_db)):
    return create_course(db, name, unit, student_id)

@app.get("/students/")
def list_students(db: Session = Depends(get_db)):
    return get_students(db)

@app.get("/courses/")
def list_courses(db: Session = Depends(get_db)):
    return get_courses(db)
