from django.db import models
from django_jalali.db import models as jmodels
from django.contrib.auth.models import User
from django.contrib.contenttypes.fields import GenericRelation
# from notification.models import Notification
# Create your models here.

class Chat(models.Model):
    topic = models.CharField(max_length=100)
    describtion = models.TextField(max_length=300)
    active = models.BooleanField(default=True)
    create = jmodels.jDateTimeField(auto_now_add=True)
    update = jmodels.jDateTimeField(auto_now=True)
    hidden = models.BooleanField(default=False)

    def __str__(self):
        return self.topic


class ChatReply(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='chat_user', null=True, blank=True)
    chat = models.ForeignKey(Chat, on_delete=models.CASCADE, related_name='chat_reply')
    name = models.CharField(max_length=20)
    site = models.URLField(blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    comment = models.TextField(max_length=500)
    is_reply = models.BooleanField(default=False)
    replay_to = models.ForeignKey('self', related_name='comment_reply',on_delete=models.CASCADE, blank=True, null=True)
    active = models.BooleanField(default=False)
    create = jmodels.jDateTimeField(auto_now_add=True)
    notify_rel = GenericRelation('notification.Notification')


    def __str__(self):
        return self.name + ' | ' + self.chat.topic

    class Meta:
        verbose_name = 'گپ'
        verbose_name_plural = 'گپ ها'