from django.contrib.auth.models import AbstractUser
from django.contrib.auth import get_user_model
from django.conf import settings
from django.db import models


class User(AbstractUser):
    ROLE_CHOICES = (
        ('student', 'Student'),
        ('teacher', 'Teacher'),
    )
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='student')


class Result(models.Model):
    user    = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    subject = models.CharField(max_length=50, blank=True, default='')
    level   = models.CharField(max_length=20, blank=True, default='')
    score   = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.user} - {self.subject}"


class Course(models.Model):
    title       = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    created_by  = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Question(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name="questions")
    title  = models.CharField(max_length=255)
    level  = models.CharField(max_length=20)

    def __str__(self):
        return self.title


class TestResult(models.Model):
    user          = models.ForeignKey(
                        settings.AUTH_USER_MODEL,
                        on_delete=models.CASCADE,
                        related_name='test_results'
                    )
    subject       = models.CharField(max_length=200)
    level         = models.CharField(max_length=100, default='Asosiy')
    score         = models.FloatField(default=0)
    stars         = models.CharField(max_length=20, default='⭐')
    finish_reason = models.CharField(max_length=20, default='manual')
    time_spent    = models.IntegerField(default=0)
    created_at    = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.user} - {self.subject} - {self.score}"