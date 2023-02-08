from django.db import models
from ckeditor.fields import RichTextField
# Create your models here.
class home(models.Model):
    d = 'd'
    p = 'p'
    STATUS_CHOICES = [
        (d, 'Draft'),
        (p, 'Published')
    ]

    title = models.CharField(max_length=120)
    description = models.TextField()
    status = models.CharField(max_length=1, choices=STATUS_CHOICES)
    image = models.ImageField(blank=True,upload_to='images/')
    def __str__(self):
        return self.title
    class Meta:
        verbose_name = 'Ana Səhifə'
        verbose_name_plural = 'Ana Səhifə'

class description (models.Model):
    sentence = RichTextField(blank=True)

    class Meta:
        verbose_name = 'Açıqlama'
        verbose_name_plural = 'Açıqlama'


    def __str__(self):
        return self.sentence

class Selector(models.Model):
    title = models.CharField(null=True,blank=True,max_length=220)
    logo2 = models.ImageField(null=True,blank=True,upload_to='images/')
    logo1 = models.ImageField(null=True,blank=True,upload_to='images/')
    logo3 = models.ImageField(null=True,blank=True,upload_to='images/')
    logo4 = models.ImageField(null=True,blank=True,upload_to='images/')
    logo5 = models.ImageField(null=True,blank=True,upload_to='images/')
    logo6 = models.ImageField(null=True,blank=True,upload_to='images/')
    logo7 = models.ImageField(null=True, blank=True, upload_to='images/')
    class Meta:
        verbose_name = 'Logolar'
        verbose_name_plural = 'Logolar'

class Social(models.Model):
    facebook = models.CharField(max_length=220)
    instagram = models.CharField(max_length=220)
    whatsapp = models.CharField(max_length=220)
    linkedin = models.CharField(max_length=220)

    class Meta:
        verbose_name = 'Sosiallar'
        verbose_name_plural = 'Sosiallar'


