# Generated by Django 4.2.5 on 2023-10-03 01:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("accounts", "0048_alter_customuser_user_type_and_more"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="customuser",
            name="photo",
        ),
        migrations.AlterField(
            model_name="lecturer",
            name="employee_number",
            field=models.CharField(
                default="HIM-LEC-228272", max_length=20, unique=True
            ),
        ),
        migrations.AlterField(
            model_name="student",
            name="student_id",
            field=models.CharField(default="HIM-71807223-2023", max_length=25),
        ),
    ]
