# todo/todo_api/urls.py : API urls.py
from django.urls import path, include
from .views import (
    practiceListApiView,
)


urlpatterns = [
    path('api', practiceListApiView.as_view()),

]