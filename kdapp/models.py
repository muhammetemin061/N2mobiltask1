from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django.contrib.auth.models import User

# Create your models here.

class  User(models.Model):
    name=models.CharField(max_length=50)
    surname=models.CharField(max_length=50)
    username=models.CharField(max_length=30,editable=True)
    email=models.EmailField( max_length=254,null=True)
    adress=models.JSONField(default=dict, null=True, help_text="Adres bilgilerini JSON formatında giriniz.")
    phone=PhoneNumberField(max_length=17,default='N/A',null=True,blank=True)
    website=models.CharField(max_length=100)
    company=models.JSONField(default=dict,null=True)
    latitude = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True) 
    longitude = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)  
    def __str__(self):
        return  f'{self.name} {self.surname}'

class  Post(models.Model):
      user=models.ForeignKey(User,on_delete=models.CASCADE,related_name='posts')
      title=models.CharField(max_length=100)
      body=models.TextField()
    
class Album(models.Model):
       user=models.ForeignKey(User,on_delete=models.CASCADE,related_name='album')
       title=models.CharField(max_length=255)
       def __str__(self):
          return  self.title

class Photo(models.Model):
       album=models.ForeignKey(Album,on_delete=models.CASCADE,related_name='photo')       
       title=models.CharField(max_length=255)
       url=models.URLField()
       thumbnailurl=models.URLField()

       def __str__(self):
        return  self.title
       
class Comment(models.Model):
    post = models.ForeignKey('Post', on_delete=models.CASCADE, related_name='comments')  
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments',null=True, blank=True) 
    name = models.CharField(max_length=255)  
    email = models.EmailField()  
    body = models.TextField()  
    created_at = models.DateTimeField(auto_now_add=True)  
    

    def __str__(self):
        return f"Comment by {self.name} on {self.post.title}"
     
class ToDo(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE,related_name="todo")
    title=models.CharField(max_length=255)
    completed=models.BooleanField(default=False)
       
    def __str__(self):
        return self.title
     