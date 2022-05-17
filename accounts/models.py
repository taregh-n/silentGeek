from django.db import models
from django.contrib.auth.models import User

# Create your models here.

# class Profile(models.Model):
#     user = models.OneToOneField(User, on_delete= models.CASCADE)
#     phone = models.IntegerField(null=True, blank= True)
#     address = models.CharField(max_length=250, null=True, blank= True)

# class SocialMedia(models.Model):
#     user = models.ForeignKey(User, on_delete= models.CASCADE, related_name='user_social')
#     social = models.TextChoices()
#     link = models.URLField()