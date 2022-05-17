from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.blog, name='blog'),
    path('post/<int:post_id>/', views.post_details, name='post'),
    path('comment/<int:post_id>/', views.post_comment, name='comment'),
    # path('reply_comment/<int:post_id>/<int:comment_id>', views.reply_to_comment, name='reply_comment'),
]