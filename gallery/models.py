from django.db import models
from django_jalali.db import models as jmodels
from django.contrib.auth.models import User

# Create your models here.

class GalleryCategory(models.Model):
    title = models.CharField(max_length=50)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.title

class GalleryPost(models.Model):
    title = models.CharField(max_length=50)
    describtion = models.TextField(max_length=400)
    category = models.ForeignKey(GalleryCategory, related_name='gallery_cat', on_delete=models.PROTECT)
    creator = models.ForeignKey(User, on_delete=models.CASCADE, related_name='gallery_creator')
    create = jmodels.jDateTimeField(auto_now_add=True)
    update = jmodels.jDateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.title

class GalleryImage(models.Model):
    post = models.ForeignKey(GalleryPost, related_name='gallery_post_img', on_delete=models.CASCADE)
    image = models.ImageField(upload_to = 'gallery')
    create = jmodels.jDateTimeField(auto_now_add=True)
    update = jmodels.jDateTimeField(auto_now=True)

    def __str__(self):
        return self.post.title