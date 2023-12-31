# Generated by Django 4.2.5 on 2023-10-02 23:28

import datetime
from django.db import migrations, models
import django.utils.timezone
import django_countries.fields


class Migration(migrations.Migration):
    dependencies = [
        ("accounts", "0046_remove_customuser_address_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="customuser",
            name="address",
            field=models.TextField(default=django.utils.timezone.now, null=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="customuser",
            name="church_name",
            field=models.CharField(default=django.utils.timezone.now, max_length=500),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="customuser",
            name="city",
            field=models.CharField(default=django.utils.timezone.now, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="customuser",
            name="country",
            field=django_countries.fields.CountryField(
                default=django.utils.timezone.now, max_length=20
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="customuser",
            name="date_of_birth",
            field=models.DateField(
                blank=True, default=datetime.datetime.now, null=True
            ),
        ),
        migrations.AddField(
            model_name="customuser",
            name="gender",
            field=models.CharField(
                blank=True,
                choices=[("Female", "Female"), ("Male", "Male")],
                max_length=50,
            ),
        ),
        migrations.AddField(
            model_name="customuser",
            name="nationality",
            field=models.CharField(default=django.utils.timezone.now, max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="customuser",
            name="phone",
            field=models.CharField(default=django.utils.timezone.now, max_length=15),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="customuser",
            name="photo",
            field=models.ImageField(blank=True, null=True, upload_to="user_photos/"),
        ),
        migrations.AlterField(
            model_name="lecturer",
            name="employee_number",
            field=models.CharField(
                default="HIM-LEC-824992", max_length=20, unique=True
            ),
        ),
        migrations.AlterField(
            model_name="student",
            name="student_id",
            field=models.CharField(default="HIM-48701199-2023", max_length=25),
        ),
    ]
