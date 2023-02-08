from django.db import models
from ckeditor.fields import RichTextField
# Create your models here.
class Maqala(models.Model):
    name = models.CharField(max_length=100)
    title = models.CharField(null=True,blank = True,max_length=10000)
    image = models.ImageField(null=True, blank=True, upload_to='images/')
    description = RichTextField()
    date = models.DateField(auto_now_add=True, auto_now=False, blank=True)
    facebook = models.CharField(null=True,blank=True,max_length=120)
    twitter = models.CharField(null=True,blank=True,max_length=120)
    linkedin = models.CharField(null=True,blank=True,max_length=120)

    class Meta:
        verbose_name = 'Məqalə'
        verbose_name_plural = 'Məqalə'

class Result(models.Model):
    name = models.CharField(max_length=100)
    title = models.CharField(null=True,blank = True,max_length=10000)
    image = models.ImageField(null=True, blank=True, upload_to='images/')
    description = RichTextField()
    date = models.DateField(auto_now_add=True, auto_now=False, blank=True)
    facebook = models.CharField(null=True,blank=True,max_length=120)
    twitter = models.CharField(null=True,blank=True,max_length=120)
    linkedin = models.CharField(null=True,blank=True,max_length=120)
    class Meta:
        verbose_name = 'Nəticələr'
        verbose_name_plural = 'Nəticələr'

class Members(models.Model):
    name = models.CharField(max_length=220)
    image = models.ImageField(upload_to='images/')
    description = models.TextField()
    class Meta:
        verbose_name= 'Üzvlər'
        verbose_name_plural = 'Üzvlər'