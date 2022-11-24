from rest_framework import viewsets
from rest_framework import status
from practice_api.models import Practice
from practice_api.serializers import practiceSerializer
from rest_framework import permissions
# Create your views here.


class ReadModelViewSets(viewsets.ReadOnlyModelViewSet):
    queryset = Practice.objects.all()
    serializer_class = practiceSerializer
