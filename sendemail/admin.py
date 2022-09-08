from django.contrib import admin
from . models import Post

# from .models import LikeButton #import the class from models file present in the app
# # Register your models here.
admin.site.register(Post)