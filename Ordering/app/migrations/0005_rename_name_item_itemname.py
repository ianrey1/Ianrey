# Generated by Django 5.1.3 on 2025-01-13 14:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_order_customer'),
    ]

    operations = [
        migrations.RenameField(
            model_name='item',
            old_name='name',
            new_name='itemname',
        ),
    ]
