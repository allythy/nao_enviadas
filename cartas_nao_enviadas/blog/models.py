from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import datetime, date

class Letter(models.Model):
    name = models.CharField(max_length=255)
    message = models.TextField(max_length=250)
    letter_date = models.DateField(auto_now_add=True)


    def __str__(self):
        return f"{self.name}"

    def get_absolute_url(self):
        return reverse('home')