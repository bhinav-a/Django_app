from django.db import models

# Create your models here.
class Student(models.Model):
    # id = models.AutoField()
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    email = models.EmailField(max_length=100)
    address = models.TextField( null=True , blank=True)
    # image = models.ImageField()
    file = models.FileField()
    
    def __str__(self) -> str: 
        # this function will print [<Student: Abhinav>, <Student: Aayush>]> instead of  [<Student: Student object (1)>, <Student: Student object (2)>] in the shell

        return self.name


class Car(models.Model):
    car_name = models.CharField(max_length=100)
    speed = models.IntegerField(default=50)

"""
various ways of creating a models object in shell:

1.
car = Car.objects.create(car_name = "Alto" , speed=80)

2.
car_dict = {"car_name = "XUV" , speed=90}
Car.objects.create(**car_dict)
"""