from django.db import models
from login.models import User

# Create your models here.


class Story(models.Model):
    title = models.CharField(max_length=20)
    category = models.CharField(max_length=20)
    story = models.CharField(max_length=2000)
    fk_user = models.ForeignKey(User, on_delete=models.CASCADE)
    is_beginning = models.BooleanField()

    def __str__(self):
        return self.title


class Extension(models.Model):
    fk_origin = models.ForeignKey(Story, on_delete=models.CASCADE, related_name='origin')
    fk_continuation = models.ForeignKey(Story, on_delete=models.CASCADE, related_name='continuation')
