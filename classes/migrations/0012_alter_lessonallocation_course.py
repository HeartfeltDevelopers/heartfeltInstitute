# Generated by Django 4.2.5 on 2023-10-11 17:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("classes", "0011_alter_onlinelesson_course_name"),
    ]

    operations = [
        migrations.AlterField(
            model_name="lessonallocation",
            name="course",
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
