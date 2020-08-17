from django.contrib.auth.models import User
from django.db import models
from tinymce.models import HTMLField
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.
class Techs(models.Model):
    name = models.CharField(max_length= 30)

    def __str__(self):
        return self.name

class Post(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    name = models.CharField(max_length = 60)
    url = models.CharField(max_length=120)    
    description = models.TextField()    
    screenshot = models.ImageField(upload_to = 'screenshot')
    techs = models.ManyToManyField(Techs, related_name='techs')

    def __str__(self):
        return self.name

    @classmethod
    def get_posts(cls):
        posts = cls.objects.order_by('name')
        return posts

    @classmethod
    def get_post_details(cls, id):
        post = cls.objects.filter(id = id).first()
        return post


class Kura(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    post = models.ForeignKey(Post,on_delete=models.CASCADE)
    design = models.IntegerField(default = 1,validators=[MaxValueValidator(10), MinValueValidator(1)])
    usability = models.IntegerField(default = 1,validators=[MaxValueValidator(10), MinValueValidator(1)])    
    content = models.IntegerField(default = 1,validators=[MaxValueValidator(10), MinValueValidator(1)])
    
    def __str__(self):
        return self.post

    @classmethod
    def get_post_kura(cls, id):
        kuras = cls.objects.filter(post = id)
        return kuras