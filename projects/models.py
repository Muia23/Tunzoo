from django.db import models

# Create your models here.
class Post(models.Model):
    name = models.CharField(max_length = 60)
    url = models.CharField(max_length=120)    
    description = models.TextField()    
    screenshot = models.ImageField(upload_to = 'screenshot')