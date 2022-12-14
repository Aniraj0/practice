from django.db import models

# Create your models here.
# practice/practice_api/models.py
from django.db import models
from django.contrib.auth.models import User

class Practice(models.Model):
    task = models.CharField(max_length = 180)
    timestamp = models.DateTimeField(auto_now_add = True, auto_now = False, blank = True)
    completed = models.BooleanField(default = False, blank = True)
    updated = models.DateTimeField(auto_now = True, blank = True)
    user = models.ForeignKey(User, on_delete = models.CASCADE, blank = True, null = True)
    id = models.AutoField(primary_key=True)

    def __str__(self):
        return self.task



