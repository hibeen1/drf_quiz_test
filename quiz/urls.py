from django.urls import path, include
from django.urls.resolvers import URLPattern
from .views import helloAPI, randomQuiz, showQuizAll

urlpatterns = [
    path("hello/", helloAPI),
    path("<int:id>/", randomQuiz),
    path("showall/", showQuizAll),
]