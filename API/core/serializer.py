from rest_framework import serializers
from .models import Student,College




class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields='__all__'

    def validate_age(self, value):
        if value < 18:
            raise serializers.ValidationError("Age must be at least 18.")
        return value
    
    def validate(self, data):
        if data['branch'].lower() == 'unknown':
            raise serializers.ValidationError("Branch cannot be 'unknown'.")
        return data


class CollegeSerializer(serializers.ModelSerializer):
    students = StudentSerializer(many=True, read_only=True)

    class Meta:
            model = College
            fields = ['id', 'name', 'students']