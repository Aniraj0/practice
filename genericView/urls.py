# todo/todo_api/urls.py : API urls.py
from django.urls import path, include
from rest_framework import routers
from .views import (
    genericViews,
)

from practice_api.views import (
    practiceListApiView,
)

router = routers.DefaultRouter()
router.register('genericViews', genericViews, basename='genericViews')

urlpatterns = [
    path('api', practiceListApiView.as_view()),
    path('', include(router.urls))
]