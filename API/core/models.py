from django.db import models

# Create your models here.

class College(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Student(models.Model):
    name = models.CharField(max_length=100)
    college = models.ForeignKey(College, related_name='students', on_delete=models.CASCADE)
    age = models.IntegerField()
    branch = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    

