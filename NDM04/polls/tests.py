

# Create your tests here.
import datetime

from django.test import TestCase
from django.utils import timezone

from .models import Вопрос


class ВопросModelTests(TestCase):

    def test_was_published_recently_with_future_Вопрос(self):
        """
        was_published_recently() returns False for Вопросs whose pub_date
        is in the future.
        функция was_published_recently() возвращает значение False для Bonpocs, чья дата публикации
        находится в будущем.
        
        """
        time = timezone.now() + datetime.timedelta(days=30)
        future_Вопрос = Вопрос(pub_date=time)
        self.assertIs(future_Вопрос.was_published_recently(), False)
