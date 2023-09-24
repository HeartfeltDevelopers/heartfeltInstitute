# Generated by Django 4.2.5 on 2023-09-19 05:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0024_alter_lecturer_employee_number_and_more'),
        ('courses', '0001_initial'),
        ('classes', '0004_rename_studentclass_studentclasse'),
    ]

    operations = [
        migrations.CreateModel(
            name='Choice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(max_length=500)),
                ('text', models.CharField(max_length=100)),
                ('is_correct', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(max_length=500)),
                ('marks', models.PositiveBigIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='StudentResponse',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_correct', models.BooleanField(default=False)),
                ('marks_obtained', models.PositiveBigIntegerField(default=0)),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='classes.question')),
                ('selected_choice', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='classes.choice')),
            ],
        ),
        migrations.CreateModel(
            name='StudentTestSubmission',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('submission', models.DateTimeField(auto_now_add=True)),
                ('total_score', models.PositiveBigIntegerField(default=0)),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.student')),
            ],
        ),
        migrations.CreateModel(
            name='Test',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('start_time', models.DateTimeField()),
                ('end_time', models.DateTimeField()),
                ('total_marks', models.IntegerField()),
                ('course_name', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='courses.course')),
            ],
        ),
        migrations.CreateModel(
            name='TestFeedBack',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('feedback_text', models.TextField(blank=True)),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.student')),
                ('test', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='classes.test')),
            ],
        ),
        migrations.DeleteModel(
            name='Club',
        ),
        migrations.RemoveField(
            model_name='libraryrecord',
            name='student',
        ),
        migrations.DeleteModel(
            name='SportsActivity',
        ),
        migrations.DeleteModel(
            name='LibraryRecord',
        ),
        migrations.AddField(
            model_name='studenttestsubmission',
            name='test',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='classes.test'),
        ),
        migrations.AddField(
            model_name='studentresponse',
            name='submission',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='classes.studenttestsubmission'),
        ),
        migrations.AddField(
            model_name='question',
            name='test',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='classes.test'),
        ),
    ]
