from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Course


class CourseSerializer(serializers.ModelSerializer):
    teacher = serializers.ReadOnlyField(source='teacher.username')

    class Meta:
        model = Course
        fields = ('id', 'title', 'description', 'student', 'teacher', 'duration',)


class UserSerializer(serializers.ModelSerializer):
    courses = serializers.PrimaryKeyRelatedField(many=True, queryset=Course.objects.all())

    class Meta:
        model = User
        fields = ('id', 'username', 'courses')