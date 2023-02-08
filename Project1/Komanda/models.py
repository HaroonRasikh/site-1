from django.db import models
from ckeditor.fields import RichTextField
# Create your models here.
class Komanda(models.Model):
    title = models.CharField(null=True,blank=True,max_length=10000)
    description = RichTextField(blank=True)

    def __str__(self):
        return self.title
    class Meta:
        verbose_name='Komanda'
        verbose_name_plural = 'Komanda'

class Chart(models.Model):
    title1 = models.CharField(null=True, blank=True, max_length=10000)
    title2 = models.CharField(null=True, blank=True, max_length=10000)
    description = RichTextField(blank=True)
    facebook = models.CharField(null=True, blank=True, max_length=220)
    twitter = models.CharField(null=True, blank=True, max_length=220)
    linkedin = models.CharField(null=True, blank=True, max_length=220)

    def __str__(self):
        return self.title1
    class Meta:
        verbose_name='Tablo'
        verbose_name_plural ='Tablolar'