# Generated by Django 4.1.4 on 2023-01-05 10:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("about", "0004_alter_officers_person"),
    ]

    operations = [
        migrations.AlterField(
            model_name="officers",
            name="position",
            field=models.IntegerField(
                choices=[
                    (1, "Co Chairs"),
                    (2, "Treasurer"),
                    (3, "Corresponding Secretary"),
                    (4, "Recording Secretary"),
                    (5, "Comrades At Large"),
                ]
            ),
        ),
    ]