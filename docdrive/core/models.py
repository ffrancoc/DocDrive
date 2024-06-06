from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.utils import timezone
import time
import uuid


def update_filename(instance, filename):    
    file = str(int(time.time()))
    return f'{instance.user.storage}/{file}{instance.file_type}'


class User(AbstractUser):    
    storage= models.CharField(max_length=50, blank=False, null=None, default=str(uuid.uuid4)[24:-1])


class Archive(models.Model):    
    file = models.FileField(upload_to=update_filename)    
    title = models.CharField(max_length=20, blank=False, null=None)    
    file_type = models.CharField(max_length=10, blank=False, null=None)
    file_size = models.CharField(blank=False, null=None, max_length=50)
    create_at = models.DateTimeField(null=None, default=timezone.now)
    modified = models.DateTimeField(null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def delete(self):
        self.file.delete()
        super().delete()

# class Media(models.Model):
#     location = models.CharField(max_length=200, blank=False, null=None, unique=True)
#     archive = models.ForeignKey(Archive, on_delete=models.CASCADE)
