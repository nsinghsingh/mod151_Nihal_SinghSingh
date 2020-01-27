from django.db import models
from login.models import User

# Create your models here.


class Story(models.Model):
    title = models.CharField(max_length=20)
    category = models.CharField(max_length=20)
    story = models.CharField(max_length=2000)
    fk_user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
