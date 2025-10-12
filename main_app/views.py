
from django.shortcuts import render, redirect
from .models import Quiz, Question
from .forms import QuizForm, QuestionForm

# Create your views here.

# def home(request):
#     return HttpResponse('My FULL-stack PROJECT Using DJANGO')

# def home(request):
#     return render('home.html')

def base(request):
    return render(request , 'base.html')

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

# Question List + Create
def question_list(request, quiz_id):
    quiz = Quiz.objects.get(id=quiz_id)
    questions = quiz.questions.all()
    if request.method == 'POST':
        form = QuestionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('question_list', quiz_id=quiz_id)
    else:
        form = QuestionForm(initial={'quiz': quiz})
    return render(request, 'question_list.html', {'quiz': quiz, 'questions': questions, 'form': form})
