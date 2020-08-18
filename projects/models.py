from django.contrib.auth.models import User
from django.db import models
from tinymce.models import HTMLField
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db.models import Avg,F

# Create your models here.
class Techs(models.Model):
    name = models.CharField(max_length= 30)

    def __str__(self):
        return self.name

class Profile(models.Model):
    profile_pic = models.ImageField(upload_to = 'profile')
    username = models.CharField(max_length = 60)
    bio = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)    

    def __str__(self):
        return self.username

    @classmethod
    def get_profile(cls, id):
        profile = cls.objects.filter(id = id).first()
        return profile
        

class Post(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    user = models.ForeignKey(Profile,on_delete=models.CASCADE)
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
    
    @classmethod
    def get_average(cls, id):
        avrg = cls.objects.filter(post = id)
        avrg.aggregate(avr = Avg(F('design') + F('usability')+ F('content')))        
        return avrg

class Comment(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    post = models.ForeignKey(Post,on_delete=models.CASCADE)
    comment = HTMLField()

    def __str__(self):
        return self.comment

    @classmethod
    def get_comments(cls, id):
        comments = cls.objects.filter(post = id)
        return comments