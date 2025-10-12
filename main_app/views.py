from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login
from django.contrib.auth.views import LoginView
from .models import Quiz, Question, Profile
from .forms import SignUpForm, QuizForm, QuestionForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User



def base(request):
    return render(request, 'base.html')


def signup(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            Profile.objects.create(
                user=user, user_type=form.cleaned_data['user_type'])
            login(request, user)
            return redirect('base')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})


class CustomLoginView(LoginView):
    template_name = 'login.html'

@login_required
def quiz_list(request):
    quizzes = Quiz.objects.all()
    if request.method == 'POST':
        form = QuizForm(request.POST)
        if form.is_valid():
            quiz = form.save(commit=False)
            quiz.user = request.user
            quiz.save()
            return redirect('quiz_list')
    else:
        form = QuizForm()
    return render(request, 'quiz_list.html', {'quizzes': quizzes, 'form': form})

# Question list + create

@login_required
def question_list(request, quiz_id):
    quiz = get_object_or_404(Quiz, id=quiz_id)
    questions = quiz.questions.all()
    if request.method == 'POST':
        form = QuestionForm(request.POST)
        if form.is_valid():
            question = form.save(commit=False)
            question.quiz = quiz
            question.save()
            return redirect('question_list', quiz_id=quiz_id)
    else:
        form = QuestionForm()
    return render(request, 'question_list.html', {'quiz': quiz, 'questions': questions, 'form': form})

# views.py
def profile_view(request, username):
    user = get_object_or_404(User, username=username)
    try:
        profile = user.profile
    except Profile.DoesNotExist:
        profile = None  # أو اعمل redirect أو show رسالة
    return render(request, 'profile.html', {'profile': profile, 'user': user})
