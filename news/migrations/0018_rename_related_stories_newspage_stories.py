# Generated by Django 4.1.4 on 2022-12-13 01:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("news", "0017_alter_newspage_related_stories"),
    ]

    operations = [
        migrations.RenameField(
            model_name="newspage",
            old_name="related_stories",
            new_name="stories",
        ),
    ]
