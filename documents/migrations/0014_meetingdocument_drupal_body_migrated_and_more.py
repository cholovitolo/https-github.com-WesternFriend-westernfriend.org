# Generated by Django 4.2.1 on 2023-06-22 19:58

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("documents", "0013_alter_publicboarddocument_category"),
    ]

    operations = [
        migrations.AddField(
            model_name="meetingdocument",
            name="drupal_body_migrated",
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="meetingdocument",
            name="drupal_path",
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name="publicboarddocument",
            name="drupal_body_migrated",
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="publicboarddocument",
            name="drupal_path",
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
