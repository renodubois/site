# Generated by Django 4.1.4 on 2022-12-30 13:11

from django.db import migrations
import wagtail.blocks
import wagtail.fields


class Migration(migrations.Migration):

    dependencies = [
        ("news", "0030_alter_story_copy"),
    ]

    operations = [
        migrations.AlterField(
            model_name="story",
            name="copy",
            field=wagtail.fields.StreamField(
                [("description", wagtail.blocks.RichTextBlock())],
                blank=True,
                null=True,
                use_json_field=True,
            ),
        ),
    ]