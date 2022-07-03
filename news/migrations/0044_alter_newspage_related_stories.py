# Generated by Django 3.2.13 on 2022-07-03 09:22

from django.db import migrations
import news.models
import wagtail.blocks
import wagtail.fields
import wagtail.images.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0043_alter_newspage_main_story_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newspage',
            name='related_stories',
            field=wagtail.fields.StreamField([('related_story', wagtail.blocks.StructBlock([('related_story_heading', wagtail.blocks.CharBlock(form_classname='full title')), ('related_story_copy', wagtail.blocks.TextBlock()), ('related_story_image', wagtail.images.blocks.ImageChooserBlock())]))], blank=True, default=news.models.upcoming_events_as_related_stories, null=True, use_json_field=True),
        ),
    ]
