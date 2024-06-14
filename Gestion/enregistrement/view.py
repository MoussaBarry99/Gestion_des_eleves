from django.urls import path
from . import views

urlpatterns = [
    path('students/', views.student_list, name='student_list'),
    path('students/create/', views.student_create, name='student_create'),
    path('enrollments/create/', views.enrollment_create, name='enrollment_create'),
]
