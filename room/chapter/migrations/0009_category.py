# Generated by Django 5.0.7 on 2024-07-25 16:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chapter', '0008_userorder'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, null=True)),
                ('describtion', models.TextField(max_length=1000, null=True)),
            ],
        ),
    ]
