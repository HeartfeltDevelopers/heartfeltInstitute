# Generated by Django 4.2.5 on 2023-09-26 18:26

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("accounts", "0027_alter_customuser_country_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="customuser",
            name="user_type",
            field=models.CharField(
                choices=[
                    ("admin", "Admin"),
                    ("lecturer", "Lecturer"),
                    ("student", "Student"),
                    ("alumni", "Alumni"),
                    ("partner", "Partner"),
                ],
                default="student",
                max_length=20,
            ),
        ),
        migrations.AlterField(
            model_name="lecturer",
            name="employee_number",
            field=models.CharField(
                default="HIM-LEC-325145", max_length=20, unique=True
            ),
        ),
        migrations.AlterField(
            model_name="student",
            name="student_id",
            field=models.CharField(default="HIM-29229959-2023", max_length=25),
        ),
    ]
