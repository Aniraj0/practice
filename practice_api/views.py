from django.shortcuts import render


from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions
from .models import Practice
from .serializers import practiceSerializer

# Create your views here.

class practiceListApiView(APIView):
    # add permission to check if user is authenticated 
    permission_classes = [permissions.IsAuthenticated]

    #1. List all

    def get(self, request, *args, **kwargs):

        # List all the practice items from given requested user

        todoo = Practice.objects.filter(user = request.user.id)
        serializer = practiceSerializer(todoo, many = True)
        return Response(serializer.data, status=status.HTTP_200_OK)


    #2. Create

    def post(self, requesst, *args, **kwargs):
        # Create the practice with given todo data

        data = {
            'task': requesst.data.get('task'),
            'completed': requesst.data.get('completed'),
            'user': requesst.user.id
        }

        serializer = practiceSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
