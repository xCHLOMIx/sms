# Generated by Django 5.1.3 on 2024-11-11 07:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0003_productin_productout'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='productin',
            name='totalPrice',
        ),
        migrations.RemoveField(
            model_name='productout',
            name='totalPrice',
        ),
    ]
