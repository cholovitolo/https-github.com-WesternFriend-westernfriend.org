# Generated by Django 4.2.6 on 2023-10-25 16:45

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("orders", "0003_order_paypal_order_id"),
    ]

    operations = [
        migrations.AddField(
            model_name="order",
            name="paypal_payment_id",
            field=models.CharField(blank=True, default="", max_length=255),
        ),
    ]
