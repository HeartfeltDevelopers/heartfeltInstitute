# Generated by Django 4.2.5 on 2023-09-19 02:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0019_alter_lecturer_employee_number_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lecturer',
            name='employee_number',
            field=models.CharField(default='HIM-LEC-928125', max_length=20, unique=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='student_id',
            field=models.CharField(default='HIM-87172904-2023', max_length=25),
        ),
    ]
