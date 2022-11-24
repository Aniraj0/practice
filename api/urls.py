# practice/api/urls.py : API urls.py
from django.urls import path, include
from .views import (
    practiceDetailApiView,
)
from practice_api.views import (
    practiceListApiView,
)


urlpatterns = [
    path('api', practiceListApiView.as_view()),
    path('api/<int:todo_id>/', practiceDetailApiView.as_view()),
]