from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.
class Ugur(models.Model):
    name = models.CharField(max_length=100)
    title1 = models.CharField(null=True,blank = True,max_length=10000)
    title2 = models.CharField(null=True,blank=True,max_length=10000)
    description1 = models.TextField(null=True,blank=True)
    image = models.ImageField(null=True, blank=True, upload_to='images/')
    description2 = RichTextField()
    date = models.DateField(auto_now_add=True, auto_now=False, blank=True)
    file = models.FileField(upload_to='files/',null=True)
    facebook = models.CharField(null=True,blank=True,max_length=120)
    twitter = models.CharField(null=True,blank=True,max_length=120)
    linkedin = models.CharField(null=True,blank=True,max_length=120)

    class Meta:
        verbose_name = 'Uğur Hekayəsi'
        verbose_name_plural = 'Uğur Hekayələri'

class hesabat(models.Model):
    
    name = models.CharField(max_length=100)
    title1 = models.CharField(null=True,blank = True,max_length=10000)
    title2 = models.CharField(null=True,blank=True,max_length=10000)
    description1 = models.TextField(null=True,blank=True)
    image = models.ImageField(null=True, blank=True, upload_to='images/')
    description2 =RichTextField()
    date = models.DateField(auto_now_add=True, auto_now=False, blank=True)
    file = models.FileField(upload_to='files/',null=True)
    facebook = models.CharField(null=True,blank=True,max_length=120)
    twitter = models.CharField(null=True,blank=True,max_length=120)
    linkedin = models.CharField(null=True,blank=True,max_length=120)

    class Meta:
        verbose_name = 'hesabat'
        verbose_name_plural = 'hesabat'

class Manager(models.Model):
    name = models.CharField(max_length=220)
    image = models.ImageField(upload_to='images/')
    description = models.TextField()

    class Meta:
        verbose_name = 'Rəhbər'
        verbose_name_plural = 'Rəhbərlər'
    