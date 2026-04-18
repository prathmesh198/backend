

# Create your models here.
from django.db import models

class Post(models.Model):
    user = models.CharField(max_length=100)
    image = models.URLField()
    caption = models.TextField()
    likes = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user