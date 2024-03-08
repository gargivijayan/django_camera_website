from django.db import models

# Create your models here.

class blog (models.Model):
    brand=models.CharField(max_length=100)
    image=models.ImageField(upload_to='article_images/')
    
    price=models.CharField(max_length=100) 
   
    description=models.CharField(max_length=300)
    date=models.DateField()
    
