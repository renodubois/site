# Generated by Django 3.2.13 on 2022-07-03 09:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0045_alter_newspage_related_stories'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newspage',
            name='main_story_image',
            field=models.ImageField(blank=True, null=True, upload_to='media/'),
        ),
    ]