# Generated by Django 4.2.5 on 2023-10-10 19:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("lecturers", "0005_assignmentnotification_date_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="assignmentnotification",
            name="notify_class",
            field=models.IntegerField(),
        ),
    ]
