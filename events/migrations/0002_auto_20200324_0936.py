# Generated by Django 3.0.4 on 2020-03-24 14:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='event',
            old_name='actionnetwork_link',
            new_name='actionnetwork_url',
        ),
    ]