# Generated by Django 5.0.7 on 2024-07-27 11:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('chapter', '0012_remove_order_customer_remove_order_product_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Category',
        ),
        migrations.DeleteModel(
            name='UserOrder',
        ),
    ]
