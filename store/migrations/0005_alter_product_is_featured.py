# Generated by Django 4.2.4 on 2023-08-23 17:25

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("store", "0004_product_is_featured"),
    ]

    operations = [
        migrations.AlterField(
            model_name="product",
            name="is_featured",
            field=models.BooleanField(default=False, null=True),
        ),
    ]
