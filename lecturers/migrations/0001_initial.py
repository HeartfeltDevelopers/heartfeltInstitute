# Generated by Django 4.2.5 on 2023-10-21 12:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('assignments', '0001_initial'),
        ('classes', '0009_remove_studentclasse_class_teacher_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='AssignmentNotification',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('notification_title', models.CharField(max_length=100)),
                ('message', models.TextField(blank=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('assignment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='assignments.assignment')),
                ('notify_class', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='notifications', to='classes.studentclasse')),
            ],
        ),
    ]
