from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'students', views.StudentViewSet, basename='student')

urlpatterns = [
    path("", views.home, name='home'),
    path('cars/', views.list_of_cars, name="list_of_cars"),
    path('bus/', views.list_of_bus, name="list_of_bus"),
    path("todos/", views.todos, name="Todos"),
    path("students/", views.students, name="students"),  # Your normal template view

    path('api/', include(router.urls)),  # API endpoints here
]
