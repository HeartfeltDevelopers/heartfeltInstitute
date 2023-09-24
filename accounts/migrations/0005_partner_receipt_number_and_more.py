# Generated by Django 4.2.5 on 2023-09-10 06:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_remove_student_attendance_records_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='partner',
            name='receipt_number',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='lecturer',
            name='employee_number',
            field=models.CharField(default='HIM-LEC-126049', max_length=10, unique=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='student_id',
            field=models.CharField(default='HIM-98635048-2023', max_length=25),
        ),
    ]
