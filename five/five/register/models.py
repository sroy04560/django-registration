from django.db import models

from django.contrib.auth.models import User
# Create your models here.

class UserModels(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE,)

    # additional feild

    site=models.URLField(blank=True)
    # blank =true means if u dosen't want to give ur url then its ok

    pics=models.ImageField(upload_to='profile_pics',blank=True)

    def __str__(self):
        return self.user.username