from django.db import models

# 퀴즈 모델 생성
class Quiz(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()
    answer = models.IntegerField()

    def __str__(self):
        return self.title