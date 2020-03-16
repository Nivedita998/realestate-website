from django.db import models
from django.urls import reverse
# Create your models here.

class Post(models.Model):
    title=models.CharField( max_length=100)
    address=models.TextField()
    price=models.IntegerField(default=0)
    beds=models.IntegerField(default=0)
    bath=models.IntegerField(default=0)
    squarefit=models.IntegerField(default=0)
    thumbnail=models.ImageField(default='')
    thumbnail1=models.ImageField(default='')
    thumbnail2=models.ImageField(default='')
    hometype=models.CharField(max_length=50)
    pricepersquarefit=models.IntegerField(default=0)
    squarefit=models.IntegerField(default=0)
    date =models.IntegerField(default=0)
    content = models.TextField(blank=True) 


    def __str__(self):
        return self.title
    def get_absolute_url(self):
        return reverse('property_detail' , kwargs={
            'id':self.id

        })
    
    
class Contact(models.Model):
    name = models.CharField( max_length=50)
    email= models.EmailField()
    phone = models.CharField(max_length=12)
    message=models.CharField( max_length=2000 )

    def __str__(self):
        return self.email

class ContactAgent(models.Model):
    name = models.CharField( max_length=50)
    email= models.EmailField()
    phone = models.CharField(max_length=12)

    def __str__(self):
        return self.name
    










