from django.db import models

# Create your models here.
class title (models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()

    class Meta:
        verbose_name = 'başlıq'
        verbose_name_plural = 'başlıq'
class service1(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField(null=True, blank=True, upload_to="images/")
    about = models.TextField(null = True,blank=True)
    def __str__(self):
        return self.name
    class Meta:
        verbose_name = 'tablo (1)'
        verbose_name_plural = 'tablo (1)'



class service2(models.Model):
    '''
    d = 'd'
    p = 'p'
    STATUS_CHOICES = [
        (d, 'Draft'),
        (p, 'Published')
    ]
    '''
    subject = models.CharField(max_length=255)
    description = models.TextField()
    #status = models.CharField(max_length=1, choices=STATUS_CHOICES)
    def __str__(self):
        return self.subject
    class Meta:
        verbose_name = 'tablo (2)'
        verbose_name_plural = 'tablo (2)'



class service3(models.Model):
    '''
    d = 'd'
    p = 'p'
    STATUS_CHOICES = [
        (d, 'Draft'),
        (p, 'Published')
    ]
    '''
    subject = models.CharField(max_length=255)
    description = models.TextField()
    #status = models.CharField(max_length=1, choices=STATUS_CHOICES)
    def __str__(self):
        return self.subject
    class Meta:
        verbose_name= 'tablo (3)'
        verbose_name_plural = 'tablo (3)'

class service4(models.Model):
    '''
    d = 'd'
    p = 'p'
    STATUS_CHOICES = [
        (d, 'Draft'),
        (p, 'Published')
    ]
    '''
    subject = models.CharField(max_length=255)
    description = models.TextField()
    #status = models.CharField(max_length=1, choices=STATUS_CHOICES)
    def __str__(self):
        return self.subject
    class Meta:
        verbose_name= 'tablo (4)'
        verbose_name_plural = 'tablo (4)'