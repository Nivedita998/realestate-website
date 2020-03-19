from django.db import models
from ckeditor.fields import RichTextField
from django.contrib.auth import get_user_model
from django.urls import reverse
# Create your models here.
User=get_user_model()

class Author(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    #profile_picture=models.ImageField()

    
    def __str__(self):
        return self.user.username

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
    


class Blogpost_details(models.Model):
    title=models.CharField(max_length=100)
    overview=models.TextField()
    author=models.ForeignKey(Author,on_delete=models.CASCADE)
    #Timestamp=models.DateTimeField( auto_now_add=True)
    date =models.DateTimeField()
    blog_thumbnail=models.ImageField()
    content =RichTextField(blank=True,null=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog_details' , kwargs={
            'id':self.id

        })








