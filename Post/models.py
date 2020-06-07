from django.db import models
from django.contrib.auth.models import User
# Create your models here.
import datetime
from django.utils  import timezone


#3 user - title - img - content - created

class Post(models.Model):
    #user = models.ForeignKey(User, on_delete='None')
    user = models.ForeignKey(User,null=True,on_delete=models.SET_NULL)
    title = models.CharField(max_length=50)
    content = models.TextField(default=' ')
    img = models.ImageField(upload_to='post_img/',default='post_img/default.png')
    created = models.DateTimeField(default=timezone.now)
    active = models.BooleanField(default=True)
    def __str__(self):
        return self.title
    