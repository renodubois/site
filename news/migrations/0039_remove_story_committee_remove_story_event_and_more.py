# Generated by Django 4.1.4 on 2022-12-30 21:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("news", "0038_alter_newspagerelatedstories_page"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="story",
            name="committee",
        ),
        migrations.RemoveField(
            model_name="story",
            name="event",
        ),
        migrations.DeleteModel(
            name="NewsPageRelatedStories",
        ),
        migrations.DeleteModel(
            name="Story",
        ),
    ]
