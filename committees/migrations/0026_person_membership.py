# Generated by Django 3.1.8 on 2021-08-09 07:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('committees', '0025_remove_committeepage_leader_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='membership',
            field=models.TextField(blank=True, choices=[('Active', 'Active'), ('In Arrears', 'In Arrears'), ('LAPSED', 'Lapsed'), ('None', 'None')], null=True),
        ),
    ]
