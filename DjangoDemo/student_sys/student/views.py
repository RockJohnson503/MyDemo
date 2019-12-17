from django.views import View
from django.urls import reverse
from django.shortcuts import render, redirect

from .models import Student
from .forms import StudentForm


class IndexView(View):
    template_name = 'index.html'

    def get_context(self):
        students = Student.get_all()
        return {
            'students': students,
        }

    def get(self, request):
        context = self.get_context()
        form = StudentForm()
        context.update({
            'form': form,
        })
        return render(request, self.template_name, context=context)

    def post(self, request):
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('student:index'))
        context = self.get_context()
        context.update({
            'form': form,
        })
        return render(request, self.template_name, context=context)
