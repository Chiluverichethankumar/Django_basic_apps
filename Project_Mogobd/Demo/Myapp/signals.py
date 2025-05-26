from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from .models import Student
from pymongo import MongoClient

# MongoDB connection
client = MongoClient("mongodb://localhost:27017/")
db = client["Django_DB"]
collection = db["demodata"]

@receiver(post_save, sender=Student)
def sync_student_to_mongo(sender, instance, **kwargs):
    data = {
        "name": instance.name,
        "roll": instance.roll,
        "branch": instance.branch,
        "email": instance.email,
        "phone": instance.phone,
    }
    # Upsert student data based on 'roll'
    collection.update_one({"roll": instance.roll}, {"$set": data}, upsert=True)

@receiver(post_delete, sender=Student)
def delete_student_from_mongo(sender, instance, **kwargs):
    # Delete student from MongoDB on ORM delete
    collection.delete_one({"roll": instance.roll})
