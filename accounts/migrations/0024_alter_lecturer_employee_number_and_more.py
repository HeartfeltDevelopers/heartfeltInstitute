# Generated by Django 4.2.5 on 2023-09-19 05:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0023_alter_lecturer_employee_number_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lecturer',
            name='employee_number',
            field=models.CharField(default='HIM-LEC-466362', max_length=20, unique=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='student_id',
            field=models.CharField(default='HIM-55446780-2023', max_length=25),
        ),
    ]
