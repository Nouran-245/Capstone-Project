from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView
from django.contrib.auth.decorators import login_required
from .views import (
    CustomLoginView,
    QuizListView,
    QuizCreateView,
    QuizUpdateView,
    QuizDeleteView,
    QuestionListView,
    QuestionCreateView,
    QuestionUpdateView,
    QuestionDeleteView,
    ChoiceListView,
    ChoiceCreateView,
    ChoiceUpdateView,
    ChoiceDeleteView,
    profile_view,
)    

urlpatterns = [
    # Normal views
    path('', views.main, name='main'),
    path('homepage/', views.homepage, name='homepage'),
    path('quizzes/', QuizListView.as_view(), name='quiz_list'),
    path('profile/<str:username>/', views.profile_view, name='profile'),

    # Authentication views
    path('login/', CustomLoginView.as_view(), name='login'),
    path('signup/', views.signup, name='signup'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),

    # Quiz Crud views
    path('quizzes/add/', QuizCreateView.as_view(), name='quiz_add'),  # view to add quiz
    path('quizzes/<int:quiz_id>/update/', QuizUpdateView.as_view(), name='quiz_update'),  # view to update quiz
    path('quizzes/<int:quiz_id>/delete/', views.QuizDeleteView, name='quiz_confirm_delete'),  # view to delete quiz
    path('quizzes/<int:quiz_id>', views.add_quiz, name='question_list'),  # view to list questions of a quiz

    # Question Crud views
    path('quizzes/<int:quiz_id>/questions/', QuestionListView.as_view(), name='question_list'),
    path('quizzes/<int:quiz_id>/questions/add/', QuestionCreateView.as_view(), name='question_add'),
    path('quizzes/<int:quiz_id>/questions/<int:question_id>/update/', QuestionUpdateView.as_view(), name='question_update'),
    path('quizzes/<int:quiz_id>/questions/<int:question_id>/delete/', views.QuestionDeleteView, name='question_confirm_delete'),

    # Choice Crud views
    path('quizzes/<int:quiz_id>/questions/<int:question_id>/choices/', ChoiceListView.as_view(), name='choice_list'),
    path('quizzes/<int:quiz_id>/questions/<int:question_id>/choices/add/', ChoiceCreateView.as_view(), name='choice_add'),
    path('quizzes/<int:quiz_id>/questions/<int:question_id>/choices/<int:choice_id>/update/', ChoiceUpdateView.as_view(), name='choice_update'),
    path('quizzes/<int:quiz_id>/questions/<int:question_id>/choices/<int:choice_id>/delete/', views.ChoiceDeleteView, name='choice_confirm_delete'),

]   

