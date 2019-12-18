# encoding: utf-8

"""
File: adminforms.py
Author: Rock Johnson
"""
from django import forms


class PostAdminForm(forms.ModelForm):
    desc = forms.CharField(widget=forms.Textarea, label='摘要', required=False)
