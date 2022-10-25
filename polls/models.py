from datetime import datetime
import datetime
from email.policy import default
from statistics import mode
from time import timezone
from django.utils import timezone
from unittest.util import _MAX_LENGTH
from django.db import models
from django.contrib import admin

# Create your models here.
class Question(models.Model):
    question_text = models.CharField(max_length = 200)
    creation_date = models.DateTimeField("publish date")

    def __str__(self):
        return self.question_text

    @admin.display(
        boolean=True,
        ordering='creation_date',
        description='Published recently?',
    )

    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.creation_date <= now

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete = models.CASCADE)
    choice_text = models.CharField(max_length = 200)
    weight = models.IntegerField(default = 0)
    
    def __str__(self):
        return self.choice_text