from django.db import models
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.db.models.signals import post_save, pre_delete
from blog.models import Comment
from chat.models import ChatReply
# Create your models here.


class Notification(models.Model):
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')
    notify = models.CharField(max_length=50)
    seen = models.BooleanField(default= False)

    class Meta:
        indexes = [
            models.Index(fields=["content_type", "object_id"]),
        ]

    def __str__(self):
        if self.seen:
            txt = 'خوانده شده'
            f'یک {self.content_type.name} {txt}'
            return
        else:
            txt = 'خوانده نشده'
        return f'● یک {self.content_type.name} {txt}'


def new_notification(sender, **kwargs):
    if kwargs['created']:
        new_notify = Notification.objects.create(
            content_object = kwargs['instance'],
            notify = 'شما یک پیغام جدید دارید'
        )
        new_notify.save()

# def del_notification(sender, **kwargs):
#     print(kwargs['instance'])
#     notify = Notification.objects.filter(
#         content_object = kwargs['instance'],
#     )
#     notify.delete()

post_save.connect(new_notification, Comment)
post_save.connect(new_notification, ChatReply)