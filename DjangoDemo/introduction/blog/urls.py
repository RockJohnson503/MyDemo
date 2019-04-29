# encoding: utf-8

"""
File: urls.py
Author: Rock Johnson
"""
from django.urls import path

from . import views

app_name = 'blog'
urlpatterns = [
    path('detail/<int:article_id>/', views.article_detail, name='detail'),
    path('content/', views.article_content, name='content'),
    path('hello/', views.hello_world, name='hello'),
]