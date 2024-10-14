
import datetime
from django.db import models
from django.utils import timezone

# Create your models here.


class Вопрос(models.Model):
    Вопрос_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    def __str__(self):
        return self.Вопрос_text
    def was_published_recently(self):
        #return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now


class Выбор(models.Model):
    Вопрос = models.ForeignKey(Вопрос, on_delete=models.CASCADE)
    Выбор_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    def __str__(self):
        return self.Выбор_text


