from django.db import models

class TodoItem(models.Model):
    title = models.CharField(max_length=100)
    completed = models.BooleanField(default=False)

    def __str__(self):
        return self.title

# New model
class Student(models.Model):
    name = models.CharField(max_length=100)
    roll = models.IntegerField()
    branch = models.CharField(max_length=50)
    email = models.EmailField()
    phone = models.CharField(max_length=15)

    def __str__(self):
        return self.name
