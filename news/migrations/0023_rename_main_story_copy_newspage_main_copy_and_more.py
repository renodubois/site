# Generated by Django 4.1.4 on 2022-12-13 02:23

from django.db import migrations
import news.models
import wagtail.blocks
import wagtail.fields
import wagtail.images.blocks


class Migration(migrations.Migration):

    dependencies = [
        ("news", "0022_rename_main_story_image_newspage_banner_image"),
    ]

    operations = [
        migrations.RenameField(
            model_name="newspage",
            old_name="main_story_copy",
            new_name="main_copy",
        ),
        migrations.RemoveField(
            model_name="newspage",
            name="main_story_heading",
        ),
        migrations.AlterField(
            model_name="newspage",
            name="stories",
            field=wagtail.fields.StreamField(
                [
                    (
                        "related_story",
                        wagtail.blocks.StructBlock(
                            [
                                ("heading", wagtail.blocks.CharBlock(required=False)),
                                ("copy", wagtail.blocks.RichTextBlock(required=False)),
                                (
                                    "featured_image",
                                    wagtail.images.blocks.ImageChooserBlock(
                                        required=False
                                    ),
                                ),
                            ]
                        ),
                    )
                ],
                blank=True,
                default=news.models.upcoming_events_as_related_stories,
                null=True,
                use_json_field=True,
            ),
        ),
    ]
