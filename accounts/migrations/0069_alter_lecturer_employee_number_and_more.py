# Generated by Django 4.2.5 on 2023-10-10 19:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("accounts", "0068_alter_lecturer_employee_number_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="lecturer",
            name="employee_number",
            field=models.CharField(
                default="HIM-LEC-436543", max_length=20, unique=True
            ),
        ),
        migrations.AlterField(
            model_name="student",
            name="student_id",
            field=models.CharField(default="HIM-83755519-2023", max_length=25),
        ),
    ]