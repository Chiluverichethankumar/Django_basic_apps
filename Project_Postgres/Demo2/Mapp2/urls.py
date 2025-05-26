from django.urls import path
from .views import StudentListView, StudentCreateView
from . import views

urlpatterns=[
    path("",views.home,name='home'),
  path('api/students/', StudentListView.as_view(), name='student-list'),
    path('api/students/create/', StudentCreateView.as_view(), name='student-create'),
    
]