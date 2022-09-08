from django.contrib import admin
from django.urls import path
from . import views
from .views import contactView, successView

urlpatterns = [
    path("", contactView, name="contact"),
    path("success/", successView, name="success"),
    path('posts/',views.posts, name='posts'),
     path('post/<str:pk>/',views.postdetail, name='post'),
     path('like/', views.like, name="like")
]