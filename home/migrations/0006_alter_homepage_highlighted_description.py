# Generated by Django 3.2.11 on 2022-01-11 04:17

from django.db import migrations
import wagtail.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_auto_20210827_1701'),
    ]

    operations = [
        migrations.AlterField(
            model_name='homepage',
            name='highlighted_description',
            field=wagtail.core.fields.RichTextField(null=True),
        ),
    ]
