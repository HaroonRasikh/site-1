from django.db import models
from  datetime import datetime,date
# Create your models here.
from ckeditor.fields import RichTextField


############ HAQQINDA #########################

class About(models.Model):
    name = models.CharField(max_length=120)
    image = models.ImageField(null=True, blank=True, upload_to="images/")
    about = models.TextField()

    def __str__(self):
        return self.name
    class Meta:
        verbose_name = 'Haqqımda'
        verbose_name_plural = 'Haqqımda'
#### about team class ======
class about1(models.Model):

    name = models.CharField(max_length=120)
    slug= models.TextField(null=True,blank=True)
    image = models.ImageField(null=True,blank=True,upload_to='image/')
    facebook = models.CharField(null=True,blank=True,max_length=120)
    instagram = models.CharField(null=True,blank=True,max_length=120)
    twitter = models.CharField(null=True,blank=True,max_length=120)
    class Meta:
        verbose_name = 'Komandamız'
        verbose_name_plural='Komandamız'
    def __str__(self):
        return self.name



###### HIZMETLER #######



##################################### WORK(İŞ) #############################
'''
class work(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(null=True, blank=True,upload_to='images/')
    description = models.TextField()
    date = models.DateField(auto_now_add=True,auto_now=False,blank=True)
    class Meta:
        verbose_name = 'iş'
        verbose_name_plural = 'iş'
'''
########################################### work-message option ##################33
'''
class work1(models.Model):
    name = models.CharField(max_length=120)
    img = models.ImageField(upload_to='static/images/')
    slug = models.CharField(max_length=220)
'''


