from django.urls import path
from . import views

app_name = 'chat'

urlpatterns = [
    path('', views.chat, name='chat'),
    # path('replys/<int:chat_id>', views.replys, name='replys'),
    path('send_reply/<int:chat_id>', views.send_reply, name='send_reply'),
]