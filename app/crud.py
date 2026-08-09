from sqlalchemy.orm import Session
from . import models,schemas

def create_student(db:Session,student:schemas.StudentCreate):

    db_student=models.Student(
        name=student.name,
        email=student.email
    )

    db.add(db_student)
    db.commit()
    db.refresh(db_student)

    return db_student