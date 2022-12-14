
from rest_framework import serializers
from .models import Practice

class practiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Practice
        fields = ["task", "completed", "timestamp", "updated", "user", "id"]
