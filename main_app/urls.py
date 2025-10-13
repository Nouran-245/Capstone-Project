from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView
from .views import CustomLoginView, QuizListView,QuizCreateView,QuizUpdateView,QuizDeleteView,QuestionListView,QuestionCreateView,QuestionUpdateView,QuestionDeleteView,take_quiz,profile_view
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('', views.home, name='home'),
    path('quizzes/', QuizListView.as_view(), name='quiz_list'),
    path('quizzes/<int:quiz_id>/questions/', QuestionListView.as_view(), name='question_list'),
    path('signup/', views.signup, name='signup'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
    path('profile/<str:username>/', views.profile_view, name='profile'),
    path('quizzes/', QuizListView.as_view(), name='quiz_list'),
]

