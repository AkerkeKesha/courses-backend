from django.db import models
from django.contrib.auth.models import User


class Course(models.Model):
    started = models.DateTimeField(auto_now=True)
    title = models.CharField(max_length=100)
    description = models.TextField()
    student = models.ManyToManyField(User, blank=True, related_name='student')
    teacher = models.ForeignKey('auth.User', blank=True, related_name='teacher', on_delete=models.CASCADE)
    duration = models.IntegerField()

    class Meta:
        ordering = ('started',)

    def __str__(self):
        return self.title