from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    HelloView,
    StudentListCreateView,
    StudentDetailView,
    StudentRetrieveUpdateDestroyView,
    StudentViewSet,
    CollegeViewSet

)

router = DefaultRouter()
router.register(r'stu', StudentViewSet)
router.register(r'clg', CollegeViewSet)


urlpatterns = [
    path('hello/', HelloView.as_view()),
    path('students/', StudentListCreateView.as_view()),
    path('students/<int:pk>/', StudentDetailView.as_view(), name='student-detail'),
    path('students1/<int:pk>/', StudentRetrieveUpdateDestroyView.as_view()),
    path('', include(router.urls)),  # This adds /stu/, /stu/<id>/, etc.

]
