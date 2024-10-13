# Generated by Django 5.0.6 on 2024-09-10 14:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chapter', '0020_remove_classes_students_students_class_room'),
    ]

    operations = [
        migrations.AddField(
            model_name='students',
            name='amount',
            field=models.FloatField(null=True),
        ),
        migrations.AddField(
            model_name='students',
            name='payment_status',
            field=models.CharField(choices=[('Paid', 'Paid'), ('Not Paid', 'Not Paid')], max_length=50, null=True),
        ),
    ]