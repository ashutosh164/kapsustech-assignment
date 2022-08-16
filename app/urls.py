from django.contrib import admin
from django.urls import path
from .views import StudentList, StudentAdd, MarksList, \
    MarksUpdate, StudentUpdate, StudentDelete, MarkDelete, MarkAdd

urlpatterns = [
    path('', StudentList.as_view(), name='student_list'),
    path('std_add/', StudentAdd.as_view(), name='student_add'),
    path('mark_list/', MarksList.as_view(), name='mark_list'),
    path('mark_add/', MarkAdd.as_view(), name='mark_add'),
    path('mark_update/<int:pk>/', MarksUpdate.as_view(), name='mark_update'),
    path('student_update/<int:pk>/', StudentUpdate.as_view(), name='student_update'),
    path('student_delete/<int:pk>/', StudentDelete.as_view(), name='student_delete'),
    path('mark_delete/<int:pk>/', MarkDelete.as_view(), name='mark_delete'),
]





