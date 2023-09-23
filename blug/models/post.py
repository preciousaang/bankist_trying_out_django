from django.db import models

# Create your models here.


class Post(models.Model):
    id = models.BigAutoField(primary_key=True)
    title = models.CharField(verbose_name="Blug Title", max_length=255, unique=True)
    body = models.TextField(verbose_name="Blug Body")

    def __str__(self) -> str:
        return self.title
