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
        verbose_name = "department"
         

class StudentId(models.Model):
    S_Id = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.S_Id
 
class Subject(models.Model):
    subject = models.CharField(max_length=100)  
    
    def __str__(self)-> str:
        return self.subject

class Student(models.Model):
    
    department = models.ForeignKey(Department , related_name="depart" , on_delete=models.CASCADE)
    S_Id = models.OneToOneField(StudentId , on_delete=models.CASCADE , related_name="studentid")
    S_name = models.CharField(max_length=100)
    S_email = models.EmailField(unique=True)
    S_age = models.CharField(default=18 , max_length=3)
    S_address = models.TextField()   

    def __str__(self) -> str:
        return self.S_name

    class Meta :
        ordering  = ['S_name']
        verbose_name = "student"


class SubjectMarks(models.Model):
    student = models.ForeignKey(Student , on_delete=models.CASCADE , related_name="studentmarks")
    subject = models.ForeignKey(Subject , on_delete=models.CASCADE)
    marks = models.IntegerField()

    def __str__(self):
        return f'{self.student.S_name} {self.subject.subject}'

    class Meta :
        unique_together = ['student' , 'subject']

    