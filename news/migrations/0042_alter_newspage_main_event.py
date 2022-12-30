# Generated by Django 4.1.4 on 2022-12-30 21:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("events", "0025_alter_event_formation"),
        ("news", "0041_alter_newspage_main_event"),
    ]

    operations = [
        migrations.AlterField(
            model_name="newspage",
            name="main_event",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="events.event",
            ),
        ),
    ]
