# Generated by Django 4.2.5 on 2023-10-06 16:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        (
            "accounts",
            "0062_alter_lecturer_employee_number_alter_student_address_and_more",
        ),
    ]

    operations = [
        migrations.AlterField(
            model_name="lecturer",
            name="employee_number",
            field=models.CharField(
                default="HIM-LEC-748162", max_length=20, unique=True
            ),
        ),
        migrations.AlterField(
            model_name="student",
            name="student_id",
            field=models.CharField(default="HIM-73206469-2023", max_length=25),
        ),
        migrations.AlterField(
            model_name="userattributes",
            name="church_name",
            field=models.CharField(max_length=500),
        ),
    ]
