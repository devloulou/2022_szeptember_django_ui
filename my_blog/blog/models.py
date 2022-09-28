from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class PostsModel(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        db_table = 'posts'

    def __str__(self):
        return f"{self.title} - {self.author}" 

