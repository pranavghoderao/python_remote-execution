from django.db import models
import os
import subprocess
from subprocess import Popen,PIPE,STDOUT
import paramiko

# Create your models here.
class Documents(models.Model):
    title= models.CharField(max_length=50)
    description=models.CharField(max_length=100)
    document=models.FileField(upload_to='documents/')
    class Meta:
        db_table= "documents"

    
