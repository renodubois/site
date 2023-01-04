# Generated by Django 4.1.4 on 2023-01-03 10:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("events", "0006_delete_eventspage"),
        ("news", "0056_remove_newspagerelatedstory_image"),
    ]

    operations = [
        migrations.AddField(
            model_name="newspagerelatedstory",
            name="event",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="events.event",
            ),
        ),
    ]