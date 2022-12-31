# Generated by Django 4.1.4 on 2022-12-30 13:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("committees", "0051_alter_resourcespage_resources"),
        ("news", "0033_story_event"),
    ]

    operations = [
        migrations.AddField(
            model_name="story",
            name="committee",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="committees.committeepage",
            ),
        ),
    ]