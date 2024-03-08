from tabnanny import verbose
from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class FeedBack(models.Model):

    user = models.ForeignKey(
        User, on_delete=models.CASCADE, verbose_name='Пользователь', related_name = 'user_feedback')
    subject = models.CharField(max_length=200, verbose_name='Тема')
    message = models.TextField(verbose_name='Сообщение')
    date_create = models.DateTimeField(
        auto_now_add=True, verbose_name='Дата создания')

    def __str__(self):
        return f'{self.user.email} | {self.subject}'

    class Meta:
        verbose_name = 'Обратная связь'
        verbose_name_plural = 'Обратная связь'