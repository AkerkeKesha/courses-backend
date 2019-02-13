from django.db import models
from django.contrib.auth import get_user_model


User = get_user_model()


def deserialize_user(user):
    return {
        'id': user.id, 'username': user.username, 'email': user.email,
        'first_name': user.first_name, 'last_name': user.last_name
    }


class Course(models.Model):
    started = models.DateTimeField(auto_now=True)
    title = models.CharField(max_length=100)
    description = models.TextField()
    student = models.ManyToManyField(User, blank=True, related_name='student')
    teacher = models.ForeignKey(User, related_name='teacher', on_delete=models.CASCADE)
    duration = models.IntegerField()

    class Meta:
        ordering = ('started',)

    def __str__(self):
        return self.title