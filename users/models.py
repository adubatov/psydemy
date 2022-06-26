import os

from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _


def get_avatar_path(instance, filename: str):
    """
    Returns string containing path to user's avatar file in format of MEDIA_ROOT/user_{id}/avatar"""
    ext = filename.split('.')[-1]
    return f'user_{instance.id}/avatar.{ext}'


# Create your models here.
class CustomUser(AbstractUser):

    class Sex(models.IntegerChoices):
        FEMALE = 0, _('Female')
        MALE = 1, _('Male')
        __empty__ = _('(Не указан)')


    birth_date = models.DateField(blank=True, null=True)
    sex = models.IntegerField(choices=Sex.choices, null=True, blank=True)
    phone = models.CharField(max_length=12, blank=True)
    about = models.TextField(max_length=1000, blank=True, null=True)
    avatar = models.ImageField(upload_to=get_avatar_path, blank=True)

    def __str__(self):
        if self.first_name or self.last_name:
            return f'{self.first_name} {self.last_name}'
        else:
            return self.username