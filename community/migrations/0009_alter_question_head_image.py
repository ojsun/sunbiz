# Generated by Django 4.1 on 2024-01-06 11:24

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("community", "0008_question_head_image"),
    ]

    operations = [
        migrations.AlterField(
            model_name="question",
            name="head_image",
            field=models.ImageField(
                blank=True, null=True, upload_to="community/images/%Y/%m/%d/"
            ),
        ),
    ]