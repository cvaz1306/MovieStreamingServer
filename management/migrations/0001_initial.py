# Generated by Django 5.0.2 on 2024-02-11 02:56

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Movie",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.TextField()),
                ("movie", models.FileField(upload_to="")),
                ("watch_count", models.IntegerField()),
            ],
        ),
    ]