# Generated by Django 4.2.5 on 2023-10-10 19:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("lecturers", "0006_alter_assignmentnotification_notify_class"),
    ]

    operations = [
        migrations.AlterField(
            model_name="assignmentnotification",
            name="assignment",
            field=models.IntegerField(),
        ),
    ]
