# Generated by Django 4.2.5 on 2023-09-22 17:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blug', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('body', models.TextField(help_text='Sweet', null=True)),
            ],
        ),
    ]