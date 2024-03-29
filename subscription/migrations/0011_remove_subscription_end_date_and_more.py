# Generated by Django 4.2.5 on 2023-10-14 07:24

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("subscription", "0010_subscription_subscriptio_paypal__0e9eb0_idx"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="subscription",
            name="end_date",
        ),
        migrations.RemoveField(
            model_name="subscription",
            name="magazine_format",
        ),
        migrations.RemoveField(
            model_name="subscription",
            name="paid",
        ),
        migrations.RemoveField(
            model_name="subscription",
            name="price",
        ),
        migrations.RemoveField(
            model_name="subscription",
            name="price_group",
        ),
        migrations.RemoveField(
            model_name="subscription",
            name="recurring",
        ),
        migrations.RemoveField(
            model_name="subscription",
            name="start_date",
        ),
        migrations.RemoveField(
            model_name="subscription",
            name="subscriber_address_country",
        ),
        migrations.RemoveField(
            model_name="subscription",
            name="subscriber_address_locality",
        ),
        migrations.RemoveField(
            model_name="subscription",
            name="subscriber_address_region",
        ),
        migrations.RemoveField(
            model_name="subscription",
            name="subscriber_family_name",
        ),
        migrations.RemoveField(
            model_name="subscription",
            name="subscriber_given_name",
        ),
        migrations.RemoveField(
            model_name="subscription",
            name="subscriber_organization",
        ),
        migrations.RemoveField(
            model_name="subscription",
            name="subscriber_postal_code",
        ),
        migrations.RemoveField(
            model_name="subscription",
            name="subscriber_street_address",
        ),
        migrations.RemoveField(
            model_name="subscription",
            name="subscriber_street_address_line_2",
        ),
    ]
