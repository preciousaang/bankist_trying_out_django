# Generated by Django 4.2.5 on 2023-09-22 18:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blug', '0003_comment_post'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='title',
            field=models.CharField(max_length=255, unique=True, verbose_name='Blug Title'),
        ),
    ]
