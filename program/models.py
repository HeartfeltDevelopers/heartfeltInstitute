from django.db import models


class ProgramLevel(models.Model):
    level_id = models.AutoField(primary_key=True)
    level_name = models.CharField(max_length=255)


class Program(models.Model):
    program_id = models.AutoField(primary_key=True)
    program_name = models.CharField(max_length=255)
    level = models.ForeignKey(ProgramLevel, on_delete=models.CASCADE)


class Courses(models.Model):
    course_id = models.AutoField(primary_key=True)
    course_name = models.CharField(max_length=255)
    program = models.ForeignKey(Program, on_delete=models.CASCADE)
    level = models.ForeignKey(ProgramLevel, on_delete=models.CASCADE)


class Lecturer(models.Model):
    lecturer_id = models.AutoField(primary_key=True)
    lecturer_name = models.CharField(max_length=255)
    other_details = models.TextField()


class Classes(models.Model):
    class_id = models.AutoField(primary_key=True)
    class_name = models.CharField(max_length=255)
    course = models.ForeignKey(Courses, on_delete=models.CASCADE)
    lecturer = models.ForeignKey(Lecturer, on_delete=models.CASCADE)


class Students(models.Model):
    student_id = models.AutoField(primary_key=True)
    student_name = models.CharField(max_length=255)
    other_details = models.TextField()


class StudentClass(models.Model):
    student = models.ForeignKey(Students, on_delete=models.CASCADE)
    class_linked = models.ForeignKey(
        Classes, on_delete=models.CASCADE
    )  # Renamed from "class" to avoid name clash


class Assignment(models.Model):
    assignment_id = models.AutoField(primary_key=True)
    assignment_name = models.CharField(max_length=255)
    class_linked = models.ForeignKey(
        Classes, on_delete=models.CASCADE
    )  # Renamed from "class" to avoid name clash
    student = models.ForeignKey(Students, on_delete=models.CASCADE)
    lecturer = models.ForeignKey(Lecturer, on_delete=models.CASCADE)


class Lesson(models.Model):
    lesson_id = models.AutoField(primary_key=True)
    class_linked = models.ForeignKey(
        Classes, on_delete=models.CASCADE
    )  # Renamed from "class" to avoid name clash
    lecturer = models.ForeignKey(Lecturer, on_delete=models.CASCADE)
    student = models.ForeignKey(Students, on_delete=models.CASCADE)
