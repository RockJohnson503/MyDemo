# encoding: utf-8

"""
File: authenticate.py
Author: Rock Johnson
"""
from django.urls import reverse
from django.shortcuts import redirect
from django.utils.deprecation import MiddlewareMixin


class AuthenticateMiddleware(MiddlewareMixin):
    def process_request(self, request):
        if request.path.startswith(reverse('admin:index')) and request.META.get('HTTP_BLOG_AUTHOR') != 'king':
            return redirect('https://baidu.com')
