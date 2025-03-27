from .models import *
from faker import Faker
fake = Faker()
import random

def seed_db(n = 10)-> None:
    # seed users
    for i in range(n):
        depart_obj = Department.objects.all()
        random_index = random.randint(0 , len(depart_obj)-1)
        department = depart_obj[random_index]
        S_Id = f'STU-0{random.randint(100, 999)}'
        S_name = fake.name()
        S_email = fake.email()
        S_age = random.randint(20 , 30)
        S_address = fake.address()

        student_id_obj = StudentId.objects.create(S_Id = S_Id)

        student_obj = Student.objects.create(
            S_Id = student_id_obj ,
            S_name = S_name ,
            S_email = S_email ,
            S_age = S_age ,
            S_address = S_address ,
            department = department ,

        )

def create_subject_marks(n):
    try:
        student_objs = Student.objects.all()
        for student in student_objs: 
            subjects = Subject.objects.all()
            for subject in subjects:
                SubjectMarks.objects.create(
                    student = student ,
                    subject = subject ,
                    marks = random.randint(0 , 100)

                )
    except Exception as e:
        print(e)