from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Receipe(models.Model):
    user = models.ForeignKey(User , on_delete= models.SET_NULL , null=True , blank=True) 
    #cascade means if user get deleted then receipe will also get deleted
    r_name = models.CharField(max_length=255)
    r_description = models.TextField()
    r_image = models.ImageField(upload_to="images") 

class Department(models.Model):
    department = models.CharField(max_length=100)

    def __str__(self) -> str :
        return self.department
    
    class Meta :
        ordering = ['department']

class StudentId(models.Model):
    student_id = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.student_id
    

class Student(models.Model):
    
    S_Department = models.ForeignKey(Department , related_name="depart" , on_delete=models.CASCADE)
    S_Id = models.OneToOneField(StudentId , on_delete=models.CASCADE , related_name="studentid")
    S_name = models.CharField(max_length=100)
    S_email = models.EmailField(unique=True)
    S_phone = models.CharField(default=18)
    S_address = models.TextField()   

    def __str__(self) -> str:
        return self.student_name

    class Meta :
        ordering  = ['student_name']
        verbose_name = "student"
         
