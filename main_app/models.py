from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    USER_TYPES = (
        ('student', 'Student'),
        ('teacher', 'Teacher'),
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    user_type = models.CharField(max_length=10, choices=USER_TYPES)

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


QUESTION_TYPES = (
    ('MC', 'Multiple Choice'),
    ('MA', 'Multiple Answer'),
    ('SA', 'Short Answer'),
    ('LA', 'Long Answer'),
)


class Question(models.Model):

    quiz = models.ForeignKey(
        Quiz, on_delete=models.CASCADE, related_name='questions')
    text = models.TextField()
    question_type = models.CharField(
        max_length=20, choices=QUESTION_TYPES, default='00')


class Choice(models.Model):
    question = models.ForeignKey(
        Question, on_delete=models.CASCADE, related_name='choices')
    text = models.CharField(max_length=255)
    is_correct = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.text} ({'Correct' if self.is_correct else 'Wrong'})"


class StudentAnswer(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='answers')
    question = models.ForeignKey(
        Question, on_delete=models.CASCADE, related_name='student_answers')
    # If MCQ or MultiAnswer → store Choice references
    selected_choices = models.ManyToManyField(Choice, blank=True)
    # If Text question → store text response
    text_answer = models.TextField(blank=True, null=True)
    is_correct = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.user.username} - {self.question.text}"


class Result(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='results')
    quiz = models.ForeignKey(
        Quiz, on_delete=models.CASCADE, related_name='results')
    score = models.IntegerField()
    taken_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.quiz.title} ({self.score})"
