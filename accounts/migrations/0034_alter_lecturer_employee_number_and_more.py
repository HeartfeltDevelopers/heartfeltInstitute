# Generated by Django 4.2.5 on 2023-09-27 22:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0033_alter_lecturer_employee_number_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lecturer',
            name='employee_number',
            field=models.CharField(default='HIM-LEC-209764', max_length=20, unique=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='student_id',
            field=models.CharField(default='HIM-36460816-2023', max_length=25),
        ),
    ]