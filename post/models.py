from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=255)
    content = models.CharField(max_length=255)
    created = models.DateField(auto_now_add=True)
    modified = models.DateField(auto_now=True)
#     user = models.ForeignKey(User,on_delete = models.CASCADE)
#     Profile = models.ForeignKey('users.Profile' , on_delete = models.CASCADE)
     
#     photo = models.ImageField(upload_to='post/photos')
     
    
#     def __str__(self):
#         return '{} by @{}'.format(self.title,  self.user.username)
