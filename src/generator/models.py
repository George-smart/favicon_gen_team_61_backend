from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    profileimg = models.ImageField(default='profile_image/profile.svg')
    saved_icons = models.FileField(null=True, blank=True)


class ImageFavicons(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    icon_title = models.CharField(max_length=300)
    icon = models.FileField(upload_to='generated_icons', null=True)
    

class TextFavicon(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text_title = models.CharField(max_length=300)
    icon = models.FileField(upload_to='generated_icons', null=True)
    
    
