from django.contrib import admin
from.models import Notification
from django.utils.html import mark_safe
from django.urls import reverse
# Register your models here.


class NotificationAdmin(admin.ModelAdmin):
    list_display = ['__str__','content_object', 'content_type', 'object_id', 'seen']
    list_editable = ['seen', ]

    def content_object(self, obj):
        if 'blog' in str(obj.content_type):
            url = reverse('admin:blog_post_change', kwargs={'object_id': obj.content_object.post.id})
            txt = obj.content_object.post.title
        elif 'chat' in str(obj.content_type):
            url = reverse('admin:chat_chat_change', kwargs={'object_id': obj.content_object.chat.id})
            txt = obj.content_object.chat.topic
        return mark_safe(f'<a href="{url}" target="blank">{txt}</a>')


admin.site.register(Notification, NotificationAdmin)