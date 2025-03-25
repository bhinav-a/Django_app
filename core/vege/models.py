from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Receipe(models.Model):
    user = models.ForeignKey(User , on_delete= models.SET_NULL , null=True , blank=True) 
    #cascade means if user get deleted then receipe will also get deleted
    r_name = models.CharField(max_length=255)
    r_description = models.TextField()
    r_image = models.ImageField(upload_to="images") 