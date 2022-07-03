from distutils.command.upload import upload
from tabnanny import verbose
from django.db import models
from django.contrib.auth import get_user_model
# Create your models here.

User = get_user_model()

class AboutMe(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='about_me')
    text = models.TextField()
    img = models.ImageField(upload_to = 'images')
    age = models.PositiveIntegerField()
    
    def __str__(self) -> str:
        return self.user.username

    class Meta:
        verbose_name_plural = 'About Me'

class Contact(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    content = models.CharField(max_length=300)
    message = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.email


class MySiteLink(models.Model):
    name = models.CharField(max_length=300)
    link = models.TextField()
    img = models.ImageField(upload_to = 'images')

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name_plural = 'My Sites Links'



    


