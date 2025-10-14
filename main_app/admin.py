from django.contrib import admin
from .models import Quiz, Profile, Question, Choice
# Register your models here.
admin.site.register(Quiz)
admin.site.register(Profile)
admin.site.register(Question)
admin.site.register(Choice)