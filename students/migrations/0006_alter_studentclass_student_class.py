# Generated by Django 4.2.5 on 2023-10-10 19:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("students", "0005_studentclass"),
    ]

    operations = [
        migrations.AlterField(
            model_name="studentclass",
            name="student_class",
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
