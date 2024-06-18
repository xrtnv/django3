from django.contrib.auth.models import AbstractBaseUser, AbstractUser
from django.db import models


class User(AbstractUser):
    username = None
    email = models.EmailField(verbose_name='Email', unique=True, help_text="Введите Email")
    avatar = models.ImageField(verbose_name='avatar', blank=True, null=True, upload_to="users/avatars/")
    phone_number = models.CharField(verbose_name='Телефон', max_length=12, blank=True, null=True,
                                    help_text="Введите номер телефона")
    country = models.CharField(verbose_name='country', max_length=30, blank=True)

    token = models.CharField(max_length=100, verbose_name='Token', blank=True, null=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
        ordering = ['email', 'phone_number', 'country']

    def __str__(self):
        return self.email
