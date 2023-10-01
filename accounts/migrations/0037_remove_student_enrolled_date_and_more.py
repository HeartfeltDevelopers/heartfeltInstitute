# Generated by Django 4.2.5 on 2023-09-30 22:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("accounts", "0036_alter_lecturer_employee_number_and_more"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="student",
            name="enrolled_date",
        ),
        migrations.AlterField(
            model_name="lecturer",
            name="employee_number",
            field=models.CharField(
                default="HIM-LEC-921056", max_length=20, unique=True
            ),
        ),
        migrations.AlterField(
            model_name="student",
            name="student_id",
            field=models.CharField(default="HIM-87321861-2023", max_length=25),
        ),
    ]
