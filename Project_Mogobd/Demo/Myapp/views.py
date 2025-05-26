from rest_framework import viewsets, status
from rest_framework.response import Response
from pymongo import MongoClient
from bson.objectid import ObjectId
from django.shortcuts import render
from .models import TodoItem

# MongoDB Connection
client = MongoClient("mongodb://localhost:27017/")
db = client["Django_DB"]
collection = db["demodata"]

# Template views (unchanged)
def home(request):
    return render(request, "home.html")

def list_of_cars(request):
    return render(request, "list.html")

def list_of_bus(request):
    return render(request, "bus.html")

def todos(request):
    items=TodoItem.objects.all()
    return render(request, "todos.html",{'todos':items})

def students(request):
    # Fetch all students from MongoDB collection, excluding '_id' field
    students_data = list(collection.find({}, {'_id': 0}))
    
    # Pass students data to template
    return render(request, "students.html", {"students": students_data})


# REST API ViewSet
class StudentViewSet(viewsets.ViewSet):
    def list(self, request):
        students = list(collection.find({}, {'_id': 0}))
        return Response(students)

    def retrieve(self, request, pk=None):
        student = collection.find_one({"roll": int(pk)}, {'_id': 0})
        if student:
            return Response(student)
        return Response({"error": "Student not found"}, status=404)

    def create(self, request):
        data = request.data
        collection.insert_one(data)
        return Response({"message": "Student created"}, status=status.HTTP_201_CREATED)

    def update(self, request, pk=None):
        data = request.data
        result = collection.update_one({"roll": int(pk)}, {"$set": data})
        if result.matched_count == 0:
            return Response({"error": "Student not found"}, status=404)
        return Response({"message": "Student updated"})

    def partial_update(self, request, pk=None):
        data = request.data
        result = collection.update_one({"roll": int(pk)}, {"$set": data})
        if result.matched_count == 0:
            return Response({"error": "Student not found"}, status=404)
        return Response({"message": "Student partially updated"})

    def destroy(self, request, pk=None):
        result = collection.delete_one({"roll": int(pk)})
        if result.deleted_count == 0:
            return Response({"error": "Student not found"}, status=404)
        return Response({"message": "Student deleted"})
