# Generated by Django 4.1 on 2024-01-06 12:18

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("community", "0009_alter_question_head_image"),
    ]

    operations = [
        migrations.RenameField(
            model_name="question",
            old_name="head_image",
            new_name="image_file",
        ),
    ]
