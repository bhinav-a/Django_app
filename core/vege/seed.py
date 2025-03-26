from models import *
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
        S_email = fake.email
        S_age = random.randint(20 , 30)
        S_address = fake.address()
