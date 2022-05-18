from django.contrib import admin
from .models import *
# Register your models here.


class ReplyInline(admin.TabularInline):
    readonly_fields = ('user', 'name', 'chat', 'site', 'email', 'comment', 'is_reply', 'replay_to')
    exclude = ('image',)
    show_change_link = True
    model = ChatReply
    extra = 0
    max_num=0

class ChatAdmin(admin.ModelAdmin):
    inlines = [ReplyInline]


admin.site.register(Chat, ChatAdmin)

