# Generated by Django 4.1.4 on 2023-01-03 07:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("committees", "0052_alter_committeepage_options"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="committeespage",
            name="repeat_in_subnav",
        ),
        migrations.RemoveField(
            model_name="committeespage",
            name="repeated_item_text",
        ),
    ]