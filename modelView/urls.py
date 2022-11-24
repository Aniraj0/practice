# todo/todo_api/urls.py : API urls.py
from django.urls import path, include
from rest_framework import routers
from .views import (
    ModelViewSets,
)

from practice_api.views import (
    practiceListApiView,
)


router = routers.DefaultRouter()
router.register('modelView', ModelViewSets, basename='modelViews')

urlpatterns = [
    path('api', practiceListApiView.as_view()),
    path('', include(router.urls))
]