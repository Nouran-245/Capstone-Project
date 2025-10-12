from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', views.base, name='base'),
    path('quizzes/', views.quiz_list, name='quiz_list'),
    path('quizzes/<int:quiz_id>/questions/', views.question_list, name='question_list'),
    path('signup/', views.signup, name='signup'),
    path('login/', views.CustomLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
]
