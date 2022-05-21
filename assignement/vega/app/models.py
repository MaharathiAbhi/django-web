from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Messages(models.Model):
    message = models.TextField(max_length=1000)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(User,on_delete=models.CASCADE,default=None)