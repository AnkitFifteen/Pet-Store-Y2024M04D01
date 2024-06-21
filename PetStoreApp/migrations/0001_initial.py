# Generated by Django 5.0.6 on 2024-05-30 05:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Pet",
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
                ("image", models.ImageField(upload_to="media")),
                ("name", models.CharField(max_length=200)),
                ("species", models.CharField(max_length=200)),
                ("breed", models.CharField(max_length=200)),
                ("age", models.IntegerField()),
                (
                    "gender",
                    models.CharField(
                        choices=[("Male", "male"), ("Female", "female")], max_length=200
                    ),
                ),
                ("description", models.CharField(max_length=500)),
                ("price", models.FloatField()),
            ],
            options={
                "db_table": "Pet",
            },
        ),
    ]
