# Generated by Django 4.2.5 on 2023-09-30 05:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0035_merge_20230928_1849'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lecturer',
            name='employee_number',
            field=models.CharField(default='HIM-LEC-105016', max_length=20, unique=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='student_id',
            field=models.CharField(default='HIM-89419868-2023', max_length=25),
        ),
    ]