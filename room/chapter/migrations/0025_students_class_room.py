# Generated by Django 5.0.6 on 2024-09-10 19:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chapter', '0024_remove_students_class_room_remove_students_phone_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='students',
            name='class_Room',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
