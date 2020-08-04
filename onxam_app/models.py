from django.db import models
from django.conf import settings
from django.utils import timezone
import uuid


class UserProfile(models.Model):
    """ Table for user data not pertinent for login"""
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    id_number = models.CharField(max_length=50, null=False)
    department = models.CharField(max_length=100, null=False)
    sex = models.CharField(max_length=6, null=False)

    # Student only fields
    matriculation_number = models.CharField(max_length=50, null=True)
    registration_number = models.CharField(max_length=50, null=True)
    current_year = models.CharField(max_length=50, null=True)

    def __str__(self):
        return self.owner


class Quiz(models.Model):
    """ Table for quizzes """
    quiz_id = models.UUIDField(uuid.uuid4)
    quiz_creator = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    quiz_name = models.CharField(max_length=200, null=False)
    quiz_data = models.TextField(null=False)
    pass_mark = models.IntegerField(null=False)
    fail_mark = models.IntegerField(null=False)
    start_date = models.DateTimeField(null=False, blank=False)
    end_date = models.DateTimeField(null=False, blank=False)
    time_limit = models.IntegerField(default=600, null=False)
    created_date = models.DateTimeField(default=timezone.now)
    access_level = models.IntegerField()
    quiz_takers = models.TextField(null=True)
    number_attempts = models.IntegerField()

    def __str__(self):
        return self.quiz_id


class QuizResult(models.Model):
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    quiz_answers = models.TextField()
    quiz_score = models.IntegerField()
    quiz_status = models.CharField(max_length=6)
    quiz_taker = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return self.quiz_taker
