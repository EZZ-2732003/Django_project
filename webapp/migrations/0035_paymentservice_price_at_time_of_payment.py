# Generated by Django 5.1 on 2024-10-03 15:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0034_useractivity'),
    ]

    operations = [
        migrations.AddField(
            model_name='paymentservice',
            name='price_at_time_of_payment',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
        ),
    ]
