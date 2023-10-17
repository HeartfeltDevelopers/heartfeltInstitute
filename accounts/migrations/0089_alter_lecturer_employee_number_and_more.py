# Generated by Django 4.2.5 on 2023-10-17 00:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("accounts", "0088_userattributes_country_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="lecturer",
            name="employee_number",
            field=models.CharField(
                default="HIM-LEC-618559", max_length=20, unique=True
            ),
        ),
        migrations.AlterField(
            model_name="student",
            name="student_id",
            field=models.CharField(default="HIM-64110296-2023", max_length=25),
        ),
    ]
