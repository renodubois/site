# Generated by Django 3.2.6 on 2021-09-03 08:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('committees', '0034_remove_committeepage_api_key'),
    ]

    operations = [
        migrations.AddField(
            model_name='committeepage',
            name='leader_name',
            field=models.CharField(max_length=30, null=True),
        ),
    ]