# Generated by Django 5.0.7 on 2024-08-26 11:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('chapter', '0013_delete_category_delete_userorder'),
    ]

    operations = [
        migrations.CreateModel(
            name='Students',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('age', models.IntegerField()),
                ('class_room', models.CharField(max_length=50)),
                ('type', models.CharField(max_length=50)),
                ('adress', models.CharField(max_length=50)),
                ('phone', models.IntegerField()),
                ('stage', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Techers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('age', models.IntegerField()),
                ('adress', models.CharField(max_length=50)),
                ('type', models.CharField(max_length=50)),
                ('majour', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
    ]
