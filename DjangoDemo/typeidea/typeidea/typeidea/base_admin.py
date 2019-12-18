# encoding: utf-8

"""
File: base_admin.py
Author: Rock Johnson
"""
from django.contrib import admin


class BaseOwnerAdmin(admin.ModelAdmin):
    exclude = ['owner']

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        return qs.filter(owner=request.user)

    def save_model(self, request, obj, form, change):
        obj.owner = request.user
        return super().save_model(request, obj, form, change)
