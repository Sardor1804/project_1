from django.db import models
from django.conf import settings


class Course(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='tests/', null=True, blank=True)

    def __str__(self):
        return self.title


class Test(models.Model):
    LEVEL_CHOICES = (
        ('easy', 'Easy'),
        ('normal', 'Normal'),
        ('hard', 'Hard'),
    )

    title  = models.CharField(max_length=255)
    course = models.ForeignKey(
        Course,
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )
    level = models.CharField(
        max_length=20,
        choices=LEVEL_CHOICES,
        default='easy'
    )
    image      = models.ImageField(upload_to='tests/', null=True, blank=True)
    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )

    def __str__(self):
        return self.title

    def __str__(self):
        return self.title


class Question(models.Model):
    test = models.ForeignKey(
        Test,
        on_delete=models.CASCADE,
        related_name='questions'
    )
    text = models.TextField()

    def __str__(self):
        return self.text


class Option(models.Model):
    question   = models.ForeignKey(
        Question,
        on_delete=models.CASCADE,
        related_name='options'
    )
    text       = models.CharField(max_length=255)
    is_correct = models.BooleanField(default=False)

    def __str__(self):
        return self.text