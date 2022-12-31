# Generated by Django 4.1.4 on 2022-12-30 16:43

from django.db import migrations
import django.db.models.deletion
import modelcluster.fields


class Migration(migrations.Migration):

    dependencies = [
        ("news", "0037_alter_newspage_main_event"),
    ]

    operations = [
        migrations.AlterField(
            model_name="newspagerelatedstories",
            name="page",
            field=modelcluster.fields.ParentalKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="related_stories",
                to="news.newspage",
            ),
        ),
    ]