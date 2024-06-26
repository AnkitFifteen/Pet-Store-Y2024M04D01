# Generated by Django 5.0.6 on 2024-06-12 05:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("PetStoreApp", "0003_cart"),
    ]

    operations = [
        migrations.CreateModel(
            name="Order",
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
                ("ordernumber", models.CharField(max_length=100)),
                ("orderdate", models.DateField(max_length=100)),
                ("firstname", models.CharField(max_length=100)),
                ("lastname", models.CharField(max_length=100)),
                ("phoneno", models.BigIntegerField()),
                ("address", models.CharField(max_length=100)),
                ("city", models.CharField(max_length=100)),
                ("state", models.CharField(max_length=100)),
                ("pincode", models.BigIntegerField()),
                ("orderstatus", models.CharField(max_length=100)),
            ],
            options={
                "db_table": "Order",
            },
        ),
    ]
