# Generated by Django 3.2.11 on 2022-01-11 05:41

from django.db import migrations
import wagtail.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('committees', '0045_committeespage_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='committeespage',
            name='description',
            field=wagtail.core.fields.RichTextField(blank=True, null=True),
        ),
    ]