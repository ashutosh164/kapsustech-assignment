from django.shortcuts import render
from .models import Student, Marks
from django.views.generic import DeleteView, UpdateView, CreateView, ListView


class StudentList(ListView):
    model = Student
    template_name = 'student_list.html'
    context_object_name = 'student'


class StudentAdd(CreateView):
    model = Student
    fields = '__all__'
    template_name = 'student_list.html'
    context_object_name = 'student'
    success_url = '/'


class MarksList(ListView):
    model = Marks
    template_name = 'mark_list.html'
    context_object_name = 'marks'


class MarkAdd(CreateView):
    model = Marks
    fields = '__all__'
    template_name = 'mark_add.html'
    context_object_name = 'marks'
    success_url = '/mark_list/'


class MarksUpdate(UpdateView):
    model = Marks
    template_name = 'marks_update.html'
    context_object_name = 'marks'
    fields = '__all__'
    success_url = '/mark_list/'


class StudentUpdate(UpdateView):
    model = Student
    template_name = 'student_update.html'
    context_object_name = 'student'
    fields = '__all__'
    success_url = '/'


class StudentDelete(DeleteView):
    model = Student
    template_name = 'student_list.html'
    success_url = '/'


class MarkDelete(DeleteView):
    model = Marks
    template_name = 'mark_list.html'
    success_url = '/mark_list/'

