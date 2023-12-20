#!/usr/bin/env python3

from datetime import datetime

from sqlalchemy import (create_engine, desc, func,
    CheckConstraint, PrimaryKeyConstraint, UniqueConstraint,
    Index, Column, DateTime, Integer, String)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class Student(Base):
    __tablename__ = 'students'
    __table_args__ = (
        PrimaryKeyConstraint(
            'id',
            name='id_pk'),
        UniqueConstraint(
            'email',
            name='unique_email'),
        CheckConstraint(
            'grade BETWEEN 1 AND 12',
            name='grade_between_1_and_12')
    )
    Index('index_name', 'name')

    id = Column(Integer())
    name = Column(String())
    email = Column(String(55))
    grade = Column(Integer())
    birthday = Column(DateTime())
    enrolled_date = Column(DateTime(), default=datetime.now())

    def __repr__(self):
        return f"Student {self.id}: " \
            + f"{self.name}, " \
            + f"Grade {self.grade}"
# The repr() function is a special method for representing the objects in a class as a string.  
# printable representation of
    
if __name__ == '__main__':
    engine = create_engine('sqlite:///:memory:')
    Base.metadata.create_all(engine)

    # use our engine to configure a 'Session' class
    Session = sessionmaker(bind=engine)
    # use 'Session' class to create 'session' object
    session = Session()


        # creating records 
    albert_einstein = Student(
        name="Albert Einstein",
        email="albert.einstein@zurich.edu",
        grade=6,
        birthday=datetime(
            year=1879,
            month=3,
            day=14
        ),
    )

    alan_turing = Student(
        name="Alan Turing",
        email="alan.turing@sherborne.edu",
        grade=11,
        birthday=datetime(
            year=1912,
            month=6,
            day=23
        ),
    )

    session.bulk_save_objects([albert_einstein, alan_turing])
    session.commit()
    # print(f"New student ID is {albert_einstein.id}.")
    # print(f"New student ID is {alan_turing.id}.")
# bulk_save_objects() does not associate the records with the session, so we don't update our records' IDs.
    
           # read records 
    students = session.query(Student)
    print([student for student in students])
          #    using the all method 
    # students = session.query(Student).all()
    # print(students)

            # Selecting Only Certain Columns
    names = [name for name in session.query(Student.name)]
    print(names)

            #   Ordering
    students_by_name = [student for student in session.query(
            Student.name).order_by(
            Student.name)]
    print(students_by_name)
    # query returns records in tuple data type 

           #    using grades
    students_by_grade_desc = [student for student in session.query(
            Student.name, Student.grade).order_by(
            desc(Student.grade))]

    print(students_by_grade_desc)

        #    Limiting
    oldest_student = [student for student in session.query(
            Student.name, Student.birthday).order_by(
            desc(Student.grade)).limit(1)]

    print(oldest_student)

        # first() method
    oldest_student = session.query(
            Student.name, Student.birthday).order_by(
            desc(Student.grade)).first()

    print(oldest_student)

    #    filtering 
    query = session.query(Student).filter(Student.name.like('%Alan%'),
        Student.grade == 11)

    for record in query:
        print(record.name)

    #     updating 
    session.query(Student).update({
    Student.grade: Student.grade + 1
    })

    print([(
        student.name,
        student.grade
    ) for student in session.query(Student)])

    #     deleting data 
    query = session.query(
        Student).filter(
            Student.name == "Albert Einstein")        

    # retrieve first matching record as object
    albert_einstein = query.first()

    # delete record
    session.delete(albert_einstein)
    session.commit()

    # try to retrieve deleted record
    albert_einstein = query.first()
    print(albert_einstein)