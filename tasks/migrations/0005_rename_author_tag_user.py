# Generated by Django 5.0.6 on 2024-06-03 06:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("tasks", "0004_tag_author"),
    ]

    operations = [
        migrations.RenameField(
            model_name="tag",
            old_name="author",
            new_name="user",
        ),
    ]
