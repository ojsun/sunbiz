# Generated by Django 4.1 on 2024-01-03 06:45

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("service", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="birds",
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
                ("name", models.CharField(max_length=50)),
                ("target", models.CharField(max_length=100)),
                ("year", models.TimeField()),
                ("weight", models.IntegerField()),
                ("weight_c", models.IntegerField()),
            ],
        ),
        migrations.DeleteModel(
            name="M_birds",
        ),
    ]