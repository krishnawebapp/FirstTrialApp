from django.db import models
from django.utils import timezone

class Homepage(models.Model):
    IDno = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    FirstName = models.CharField(max_length=50)
    Message = models.TextField()