# Generated by Django 4.1 on 2023-03-28 09:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("service", "0006_subject"),
    ]

    operations = [
        migrations.CreateModel(
            name="Faculty",
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
                ("firstName", models.CharField(max_length=50)),
                ("lastName", models.CharField(max_length=50)),
                ("email", models.EmailField(max_length=254)),
                ("password", models.CharField(max_length=20)),
                ("address", models.CharField(max_length=50)),
                ("gender", models.CharField(max_length=50)),
                ("dob", models.DateField(max_length=20)),
                ("college_ID", models.IntegerField()),
                ("collegeName", models.CharField(max_length=50)),
                ("subject_ID", models.IntegerField()),
                ("subjectName", models.CharField(max_length=50)),
                ("course_ID", models.IntegerField()),
                ("courseName", models.CharField(max_length=50)),
            ],
            options={
                "db_table": "ORS_FACULTY",
            },
        ),
    ]
