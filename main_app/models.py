from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    USER_TYPES = (
        ('student', 'Student'),
        ('teacher', 'Teacher'),
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    user_type = models.CharField(max_length=10, choices=USER_TYPES)
    profile_image = models.URLField(max_length=500, blank=True, null=True)
    def __str__(self):
        return f"{self.user.username} ({self.user_type})"


class Quiz(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='quizzes')
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Question(models.Model):
    quiz = models.ForeignKey(
        Quiz, on_delete=models.CASCADE, related_name='questions')
    text = models.TextField()


class Choice(models.Model):
    question = models.ForeignKey(
        Question, on_delete=models.CASCADE, related_name='choices')
    text = models.CharField(max_length=255)
    is_correct = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.text} ({'Correct' if self.is_correct else 'Wrong'})"


class Result(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='results')
    quiz = models.ForeignKey(
        Quiz, on_delete=models.CASCADE, related_name='results')
    score = models.IntegerField()
    taken_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.quiz.title} ({self.score})"
