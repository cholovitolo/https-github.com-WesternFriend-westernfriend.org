# Generated by Django 4.2.4 on 2023-08-26 14:23

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("store", "0006_alter_product_is_featured"),
    ]

    operations = [
        migrations.AlterField(
            model_name="product",
            name="is_featured",
            field=models.BooleanField(default=False, null=True),
        ),
    ]
