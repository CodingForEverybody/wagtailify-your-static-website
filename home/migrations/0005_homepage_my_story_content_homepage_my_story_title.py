# Generated by Django 5.0.3 on 2024-04-02 16:26

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("home", "0004_homepage_cta_page_homepage_cta_text_homepage_cta_url"),
    ]

    operations = [
        migrations.AddField(
            model_name="homepage",
            name="my_story_content",
            field=models.TextField(blank=True, max_length=800),
        ),
        migrations.AddField(
            model_name="homepage",
            name="my_story_title",
            field=models.CharField(blank=True, default="My Story", max_length=40),
        ),
    ]
