# Generated by Django 5.1 on 2024-09-10 18:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0006_inventory'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Inventory',
        ),
    ]