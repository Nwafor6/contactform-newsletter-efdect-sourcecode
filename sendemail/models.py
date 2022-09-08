from django.db import models
from django.contrib.auth.models import User

# class Subscriber(models.Model):
#     email = models.EmailField(unique=True)
 

#     def __str__(self):
#         return self.email + " (" + ("not " if not self.confirmed else "") + "confirmed)"


from django.contrib.auth.models import User

class Post(models.Model):
    title=models.CharField(max_length=200)
    body=models.TextField()
    likes = models.ManyToManyField(
        User, related_name='like', default=None, blank=True)
    like_count = models.BigIntegerField(default='0')


    def __str__(self):
        return self.title


    @property
    def total_likes(self):
        return self.likes.count() 


# class LikeButton(models.Model):
#     content=models.TextField(null=True)
#     likes=models.ManyToManyField(User,blank=True, related_name='likes')
     
    