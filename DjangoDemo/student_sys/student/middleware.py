# encoding: utf-8

"""
File: middleware.py
Author: Rock Johnson
"""
import time

from django.shortcuts import render
from django.urls import reverse
from django.utils.deprecation import MiddlewareMixin


class TimeItMiddleware(MiddlewareMixin):
    def process_request(self, request):
        self.start_time = time.time()

    def process_view(self, request, func, *args, **kwargs):
        if request.path != reverse('student:index'):
            return None

        start = time.time()
        response = func(request)
        costed = time.time() - start
        print('process view: {:.2f}s'.format(costed))

        return response

    def process_response(self, request, response):
        costed = time.time() - self.start_time
        print('request to response cose: {:.2f}s'.format(costed))
        return response
