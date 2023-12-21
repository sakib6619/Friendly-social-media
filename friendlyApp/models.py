from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Profile(models.Model):
    RELATIONSHIP =(
        ('single','single'),
        ('married','married'),
        ('divorced','divorced'),
        ('Others','Other'),
    )
    GENDER = (
        ('Male','Male'),
        ('Female','Female'),
        ('Others','Others'),
    )
    RELIGION = (
        ('Islam','Islam'),
        ('Hindu','Hindu'),
        ('Buddha','Buddha'),
        ('Others','Others'),
    )
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    bio = models.TextField(max_length=500)
    image = models.ImageField(upload_to='profile/',default="def.png")
    coverImg = models.ImageField(upload_to='profile_cover/',default='cover.png')
    relationship = models.CharField(choices=RELATIONSHIP, max_length=150)
    phone = models.CharField(max_length=16)
    gender = models.CharField(choices=GENDER,max_length=100,)
    birth_date = models.DateField()
    address = models.CharField(max_length=500)
    religion = models.CharField(choices=RELIGION,max_length=50)
    def __str__(self):
        return self.user.username

class Post(models.Model):
    author = models.ForeignKey(Profile,on_delete=models.CASCADE)
    topic = models.CharField(max_length=200)
    content = models.TextField()
    post_image = models.ImageField(upload_to='post/',null=True,blank=True)
    date_posted = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.topic