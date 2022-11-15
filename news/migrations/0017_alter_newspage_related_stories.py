# Generated by Django 3.2.14 on 2022-07-13 08:35

from django.db import migrations
import news.models
import wagtail.blocks
import wagtail.fields
import wagtail.images.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0016_auto_20220706_2159'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newspage',
            name='related_stories',
            field=wagtail.fields.StreamField([('related_story', wagtail.blocks.StructBlock([('heading', wagtail.blocks.CharBlock(required=False)), ('copy', wagtail.blocks.TextBlock(required=False)), ('image', wagtail.images.blocks.ImageChooserBlock(required=False))]))], blank=True, default=news.models.upcoming_events_as_related_stories, null=True, use_json_field=True),
        ),
    ]