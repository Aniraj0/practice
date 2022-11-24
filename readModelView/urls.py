# todo/todo_api/urls.py : API urls.py
from django.urls import path, include
from rest_framework import routers
from .views import (
    ReadModelViewSets,
)

from practice_api.views import (
    practiceListApiView,
)


router = routers.DefaultRouter()
router.register('readModelView', ReadModelViewSets, basename='readModelView')

urlpatterns = [
    path('api', practiceListApiView.as_view()),
    path('', include(router.urls))
    # path('api/<int:todo_id>/', ReadModelViewSets.as_view()),
    
]