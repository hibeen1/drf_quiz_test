from django.db import models
from rest_framework import serializers
from .models import Quiz

# 시리얼라이즈는 JSON파일을 만들게 하여 API 통신을 가능하게 해주는 것
class QuizSerializer(serializers.ModelSerializer):
    class Meta:
        model = Quiz
        fields = ('title', 'body', 'answer')