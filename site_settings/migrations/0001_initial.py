# Generated by Django 5.0.3 on 2024-03-29 21:16

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="FooterLinkers",
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
                ("github", models.URLField(blank=True, null=True)),
                ("linkedin", models.URLField(blank=True, null=True)),
            ],
            options={
                "abstract": False,
            },
        ),
    ]
