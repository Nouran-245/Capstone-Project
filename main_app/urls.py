from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView
from .views import CustomLoginView, QuizListView, QuizCreateView, QuizUpdateView, QuizDeleteView, QuestionListView, QuestionCreateView, QuestionUpdateView, QuestionDeleteView, take_quiz, profile_view
from django.contrib.auth.decorators import login_required

urlpatterns = [
    # normal views
    path('', views.home, name='home'),
    path('quizzes/', QuizListView.as_view(), name='quiz_list'),
    path('profile/<str:username>/', views.profile_view, name='profile'),

    # authentication views
    path('login/', CustomLoginView.as_view(), name='login'),
    path('signup/', views.signup, name='signup'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),

    # quiz Crud views
    path('quizzes/add/', QuizCreateView.as_view(), name='quiz_add'), #view to add quiz
    path('quizzes/<int:quiz_id>/update/', QuizUpdateView.as_view(), name='quiz_update'), #view to update quiz
    path('quizzes/<int:quiz_id>/delete/', views.QuizDeleteView, name='quiz_confirm_delete'), #view to delete quiz
    path('quizzes/<int:quiz_id>/questions/',views.add_quiz, name='question_list'), #view to list questions of a quiz

]
