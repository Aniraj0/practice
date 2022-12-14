# from django.contrib.auth.models import User
from rest_framework import status
from practice_api.models import Practice
from practice_api.serializers import practiceSerializer
from rest_framework.viewsets import GenericViewSet
from rest_framework import permissions
from rest_framework.permissions import DjangoObjectPermissions
from rest_framework.response import Response

class genericViews(GenericViewSet):
    serializer_class = practiceSerializer
    queryset = Practice.objects.all()
    permission_classes = [DjangoObjectPermissions]




    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(serializer)

        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def list(self, request):
        serializer = self.get_serializer(self.get_queryset(), many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk):
        item = self.get_object()
        serializer = self.get_serializer(item)
        return Response(serializer.data)

    def destroy(self, request):
        item = self.get_object()
        item.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    # def get(self,request, *args, **kwargs):
    #     instance = self.get_object()
    #     serializer = self.get_serializer(instance)
    #     return Response(serializer.data)

    # def delete(self, request, *args, **kwargs):
    #     instance = self.get_object()
    #     instance.delete()
    #     return Response(status = status.HTTP_204_NO_CONTENT)