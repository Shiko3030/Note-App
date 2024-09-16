# Generated by Django 5.0.7 on 2024-07-27 12:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('chapter', '0013_delete_category_delete_userorder'),
    ]

    operations = [
        migrations.CreateModel(
            name='Note',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('page', models.TextField(max_length=1000, null=True)),
                ('date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
