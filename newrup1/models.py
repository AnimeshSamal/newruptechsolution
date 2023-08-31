from django.db import models

# Create your models here.
class Track(models.Model):
    img=models.ImageField(upload_to='slider')


class Link(models.Model):
    name=models.CharField(max_length=20)
    doc=models.FileField(upload_to='doc')
    def __str__(self):
        return self.name

class About(models.Model):
    img=models.ImageField(upload_to='photo')
    des=models.TextField()
    def __str__(self):
        return "Edit About"

class Services(models.Model):
    icon=models.CharField(max_length=30)
    title=models.CharField(max_length=30)
    des=models.TextField()
    def __str__(self):
        return self.title

class Partner(models.Model):
    img=models.ImageField(upload_to='partner')

class Photo(models.Model):
    img=models.ImageField(upload_to='photo')
    topic=models.CharField(max_length=60)
    date=models.DateTimeField(null=True)
    link=models.URLField(max_length=500,unique=True,default='',blank=True)
    def __str__(self):
        return self.topic

class Product(models.Model):
    img=models.ImageField(upload_to='product')
    topic=models.CharField(max_length=60)
    date=models.DateTimeField(null=True)
    link=models.URLField(max_length=500,unique=True,default='',blank=True)
    def __str__(self):
        return self.topic

class Achivement(models.Model):
    img=models.ImageField(upload_to='achivement')
    topic=models.CharField(max_length=60)
    date=models.DateTimeField(null=True)
    link=models.URLField(max_length=500,unique=True,default='',blank=True)
    def __str__(self):
        return self.topic

class Testimonial(models.Model):
    img=models.ImageField(upload_to='testimonial')
    name=models.CharField(max_length=50)
    pos=models.CharField(max_length=50)
    des=models.TextField(max_length=300)
    def __str__(self):
        return self.name

class Contact(models.Model):
    name=models.CharField(max_length=30)
    phone=models.IntegerField()
    email=models.EmailField()
    subject=models.CharField(max_length=50)
    message=models.TextField()
    def __str__(self):
        return self.name



