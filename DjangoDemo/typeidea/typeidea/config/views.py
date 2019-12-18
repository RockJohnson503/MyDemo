from django.shortcuts import render
from django.http import HttpResponse


def links(request):
    return HttpResponse('links')
