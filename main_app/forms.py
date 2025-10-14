from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Quiz, Question, Choice, Profile


class SignUpForm(UserCreationForm):
    USER_TYPES = (
        ('student', 'Student'),
        ('teacher', 'Teacher'),
    )
    user_type = forms.ChoiceField(choices=USER_TYPES)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2', 'user_type']


class QuizForm(forms.ModelForm):
    class Meta:
        model = Quiz
        fields = ['title', 'description']


class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ['text']
        widgets = {
            'text': forms.Textarea(attrs={'rows': 2, 'placeholder': 'Enter your question'}),
        }

    class Meta:
        model = Question
        fields = ['text']


class ChoiceForm(forms.ModelForm):
    text = forms.CharField(label="Choice Text", widget=forms.TextInput(
        attrs={'class': 'form-control'}))
    is_correct = forms.BooleanField(label="Correct?", required=False)

    class Meta:
        model = Choice
        fields = ['text', 'is_correct']
