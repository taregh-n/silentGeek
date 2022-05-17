
from django.db import models
from django_jalali.db import models as jmodels
from taggit.managers import TaggableManager
from django.contrib.auth.models import User
from ckeditor_uploader.fields import RichTextUploadingField
from django.contrib.contenttypes.fields import GenericRelation
# from notification.models import Notification
from random import sample
# Create your models here.

class Category(models.Model):
    title = models.CharField(max_length=50)
    image = models.ImageField(upload_to = 'category')
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.title

class Post(models.Model):
    title = models.CharField(max_length=70)
    category = models.ForeignKey(Category, related_name='post_cat', on_delete=models.CASCADE)
    image = models.ImageField(upload_to = 'posts/', blank = True, null= True)
    youtube_link = models.URLField(blank=True, null=True)
    description = models.TextField(max_length=300)
    content = RichTextUploadingField()
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='post_author')
    tags = TaggableManager(blank=True)
    active = models.BooleanField(default=False)
    create = jmodels.jDateTimeField(auto_now_add=True)
    update = jmodels.jDateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    
    def random_post(self):
        try:
            all_posts = list(Post.objects.all().exclude(id=self.id))
            random_pst = sample(all_posts, 1)
            return random_pst[0]
        except:
            return None


class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_comment', blank=True, null=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='post_comment')
    name = models.CharField(max_length=20)
    image = models.ImageField(upload_to = 'avatar/', default = 'static/images/avatar-default.png')
    site = models.URLField(blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    content = models.TextField(max_length=350)
    parent = models.ForeignKey('self', related_name='comment_reply',on_delete=models.CASCADE, blank=True, null=True)
    active = models.BooleanField(default=False)
    create = jmodels.jDateTimeField(auto_now_add=True)
    notify_rel = GenericRelation('notification.Notification')

    def __str__(self):
        return self.name + ' | ' + self.post.title

    class Meta:
        verbose_name = 'کامنت'
        verbose_name_plural = 'کامنت ها'