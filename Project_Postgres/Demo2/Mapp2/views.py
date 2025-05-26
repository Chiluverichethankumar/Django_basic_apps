# from django.shortcuts import render,HttpResponse
# from django.db import models
# from django.views.generic.list import ListView
# from django.views.generic.edit import CreateView
# from django.http import JsonResponse
# from django.views.generic import View
# from django.utils.decorators import method_decorator
# from django.middleware.csrf import get_token
# from django.http import HttpResponseBadRequest
# from django.shortcuts import get_object_or_404

# import json
# from .models import Student, Teacher

# # Create your views here.
# def home(request):
#     return HttpResponse("Hello Chethan lets get this work as the best one!")


# class StudentListView(ListView):
#     model = Student

#     def render_to_response(self, context, **response_kwargs):
#         students = context['object_list']
#         data = [
#             {
#                 'id': s.id,
#                 'name': s.name,
#                 'age': s.age,
#                 'teacher': s.teacher.name
#             }
#             for s in students
#         ]
#         return JsonResponse(data, safe=False)


# class StudentCreateView(CreateView):
#     model = Student
#     fields = ['name', 'age', 'teacher']

#     def dispatch(self, request, *args, **kwargs):
#         # only allow POST
#         if request.method.lower() != 'post':
#             return HttpResponseBadRequest("Only POST method allowed")
#         return super().dispatch(request, *args, **kwargs)

#     def post(self, request, *args, **kwargs):
#         try:
#             data = json.loads(request.body)
#             name = data.get('name')
#             age = data.get('age')
#             teacher_id = data.get('teacher')

#             teacher = get_object_or_404(Teacher, id=teacher_id)
#             student = Student.objects.create(name=name, age=age, teacher=teacher)

#             return JsonResponse({
#                 'message': 'Student created successfully',
#                 'student': {
#                     'id': student.id,
#                     'name': student.name,
#                     'age': student.age,
#                     'teacher': student.teacher.name
#                 }
#             }, status=201)

#         except json.JSONDecodeError:
#             return JsonResponse({'error': 'Invalid JSON'}, status=400)
#         except Exception as e:
#             return JsonResponse({'error': str(e)}, status=500)




from rest_framework import generics, status
from rest_framework.response import Response
from .models import Student, Teacher
from .serializers import StudentSerializer

from django.http import HttpResponse

def home(request):
    return HttpResponse("Hello Chethan lets get this work as the best one!")


class StudentListView(generics.ListAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


class StudentCreateView(generics.CreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)

        if serializer.is_valid():
            self.perform_create(serializer)
            return Response({
                'message': 'Student created successfully',
                'student': serializer.data
            }, status=status.HTTP_201_CREATED)

        return Response({'error': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
