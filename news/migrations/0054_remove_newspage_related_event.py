# Generated by Django 4.1.4 on 2023-01-03 03:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("news", "0053_alter_newsindexpage_options_alter_newspage_options_and_more"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="newspage",
            name="related_event",
        ),
    ]
