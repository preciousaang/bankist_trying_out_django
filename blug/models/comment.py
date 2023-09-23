from django.db import models
from .post import Post


class Comment(models.Model):
    id = models.BigAutoField(primary_key=True)
    post = models.ForeignKey(Post, null=True, on_delete=models.CASCADE)
    body = models.TextField(help_text="Sweet", null=True)
