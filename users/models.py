from django.db import models
from django.contrib.auth.models import User

class CustomUser(User):

    SEX_CHOICES = (
        (1, 'Мужской'),
        (2, 'Женский'),
    )

    sex = models.IntegerField(verbose_name='Пол', choices=SEX_CHOICES, blank=True, null=True)

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'