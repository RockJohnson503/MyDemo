# encoding: utf-8

"""
File: forms.py
Author: Rock Johnson
"""
from django import forms

from .models import Student


class StudentForm(forms.ModelForm):
    def clean_qq(self):
        cleaned_data = self.cleaned_data['qq']
        if not cleaned_data.isdigit():
            raise forms.ValidationError('qq必须是数字!')

        return int(cleaned_data)

    class Meta:
        model = Student
        fields = (
            'name', 'sex', 'profession',
            'email', 'qq', 'phone',
        )
