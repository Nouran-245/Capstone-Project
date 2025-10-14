# main_app/views.py

from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import Quiz, Question, Choice, StudentAnswer, Result, Profile
from .forms import QuizForm, QuestionForm, ChoiceForm
from django.urls import reverse_lazy, reverse
from .forms import SignUpForm


# normal views
def home(request):
    return render(request, "home.html")


@login_required
def profile_view(request, username):
    user = get_object_or_404(User, username=username)
    profile = getattr(user, "profile", None)
    return render(request, "profile.html", {"profile": profile, "user": user})


# authentication views
def signup(request):
    error_message = ""
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            user_type = form.cleaned_data.get("user_type")
            Profile.objects.create(user=user, user_type=user_type)
            login(request, user)
            return redirect('quiz_list')
        else:
            error_message = "Invalid sign up - try again."
    else:
        form = SignUpForm()
    return render(request, "signup.html", {"form": form, "error_message": error_message})


class CustomLoginView(LoginView):
    template_name = 'login.html'
    redirect_authenticated_user = True
    next_page = reverse_lazy('quiz_list')


# quiz CRUD views
    # Quiz Read View
class QuizListView(ListView):
    model = Quiz
    template_name = 'main_app/quiz_list.html'
    context_object_name = 'quizzes'

    def get_queryset(self):
        if self.request.user.profile.user_type == 'teacher':
            return Quiz.objects.filter(user=self.request.user)
        return Quiz.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = QuizForm()
        return context

    # Quiz Create View


class QuizCreateView(LoginRequiredMixin, CreateView):
    model = Quiz
    form_class = QuizForm
    template_name = "main_app/quiz_list.html"
    success_url = reverse_lazy('quiz_list')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


@login_required
def add_quiz(request, quiz_id):
    if request.method == 'POST':
        form = QuizForm(request.POST)
        if form.is_valid():
            new_quiz = form.save(commit=False)
            new_quiz.user = request.user
            new_quiz.save()
            return redirect('quiz_list')
    else:
        form = QuizForm()
    return render(request, 'main_app/question_list.html', {'form': form})

    # Quiz Update View


class QuizUpdateView(LoginRequiredMixin, UpdateView):
    model = Quiz
    fields = ['title', 'description']
    template_name = 'main_app/quiz_list.html'
    pk_url_kwarg = 'quiz_id'
    redirect_field_name = 'quiz_list'
    success_url = '/quizzes/'

    # Quiz Delete View


@login_required
def QuizDeleteView(request, quiz_id):
    quiz = get_object_or_404(Quiz, id=quiz_id)
    if request.method == "POST":
        quiz.delete()
        return redirect("quiz_list")
    return render(request, "main_app/quiz_confirm_delete.html", {"quiz": quiz})

    # Question Create View


class QuestionListView(LoginRequiredMixin, ListView):
    model = Question
    template_name = "main_app/question_list.html"
    context_object_name = "questions"

    def get_queryset(self):
        quiz_id = self.kwargs["quiz_id"]
        return Question.objects.filter(quiz_id=quiz_id)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["quiz"] = Quiz.objects.get(id=self.kwargs["quiz_id"])
        context["form"] = QuestionForm()
        return context

    # Question Create view


class QuestionCreateView(LoginRequiredMixin, CreateView):
    model = Question
    form_class = QuestionForm
    template_name = "main_app/question_list.html"

    def form_valid(self, form):
        quiz = Quiz.objects.get(id=self.kwargs["quiz_id"])
        form.instance.quiz = quiz
        return super().form_valid(form)

    def get_success_url(self):
        return reverse("question_list", kwargs={"quiz_id": self.kwargs["quiz_id"]})

    # Question Update view


class QuestionUpdateView(LoginRequiredMixin, UpdateView):
    model = Question
    fields = ['text']
    template_name = 'main_app/question_list.html'
    pk_url_kwarg = 'question_id'
    redirect_field_name = 'question_list'

    def get_success_url(self):
        return reverse("question_list", kwargs={"quiz_id": self.kwargs["quiz_id"]})

    # Question Delete view


def QuestionDeleteView(request, quiz_id, question_id):
    question = get_object_or_404(Question, id=question_id, quiz_id=quiz_id)
    if request.method == "POST":
        question.delete()
        return redirect("question_list", quiz_id=quiz_id)
    quiz = question.quiz
    return render(request, "main_app/question_confirm_delete.html", {"question": question, "quiz": quiz})


