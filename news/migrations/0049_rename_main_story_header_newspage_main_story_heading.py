# Generated by Django 3.2.13 on 2022-07-03 10:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0048_alter_newspage_main_story_image'),
    ]

    operations = [
        migrations.RenameField(
            model_name='newspage',
            old_name='main_story_header',
            new_name='main_story_heading',
        ),
    ]