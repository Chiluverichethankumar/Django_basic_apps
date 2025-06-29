# from django.shortcuts import render

# # Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics,viewsets
from .models import Student, College
from .serializer import StudentSerializer, CollegeSerializer
from django.shortcuts import get_object_or_404

class HelloView(APIView):
    def get(self, request):
        return Response({"message":"Hello, chethan! Welcome to DRF!"})
    

# create and read all
class StudentListCreateView(generics.ListCreateAPIView):
    queryset=Student.objects.all()
    serializer_class=StudentSerializer


class StudentDetailView(APIView):
    def get(self,request,pk):
        student = get_object_or_404(Student, id=pk)
        serializer=StudentSerializer(student)
        return Response(serializer.data)

# Read one, update, Delete 
class StudentRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Student.objects.all()
    serializer_class=StudentSerializer

class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer



class CollegeViewSet(viewsets.ModelViewSet):
    queryset = College.objects.all()
    serializer_class = CollegeSerializer