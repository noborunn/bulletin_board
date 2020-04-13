from accounts.models import CustomUser
from django.db import models
#from .validate import validate_admin

# Create your models here.


class Room(models.Model):
    title = models.CharField(verbose_name='タイトル', max_length=100)
    created_at = models.DateTimeField(verbose_name='樹立日時', auto_now_add=True)


class Message(models.Model):
    user = models.ForeignKey(CustomUser, verbose_name='ユーザー', on_delete=models.PROTECT)
    room = models.ForeignKey(Room, verbose_name='ルーム', on_delete=models.CASCADE)
    content = models.TextField(verbose_name='本文')
    created_at = models.DateTimeField(verbose_name='作成日時', auto_now_add=True)

