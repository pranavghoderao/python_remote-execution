from django.db import models

# Create your models here.
class Documents(models.Model):
    title= models.CharField(max_length=50)
    description=models.CharField(max_length=100)
    document=models.FileField(upload_to='documents/')
    class Meta:
        db_table= "documents"
