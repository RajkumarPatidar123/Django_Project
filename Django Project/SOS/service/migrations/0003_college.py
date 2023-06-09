# Generated by Django 4.1 on 2023-03-24 04:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("service", "0002_role"),
    ]

    operations = [
        migrations.CreateModel(
            name="College",
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
                ("collegeName", models.CharField(max_length=50)),
                ("collegeAddress", models.CharField(max_length=50)),
                ("collegeState", models.CharField(max_length=50)),
                ("collegeCity", models.CharField(max_length=20)),
                ("collegePhoneNumber", models.CharField(max_length=20)),
            ],
            options={
                "db_table": "ORS_COLLEGE",
            },
        ),
    ]
