# Generated by Django 4.1.4 on 2023-01-05 10:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("about", "0002_alter_officers_position"),
    ]

    operations = [
        migrations.AlterField(
            model_name="officers",
            name="email",
            field=models.EmailField(blank=True, max_length=254, null=True),
        ),
    ]