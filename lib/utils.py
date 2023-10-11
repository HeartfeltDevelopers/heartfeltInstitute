from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseRedirect
from django.db import connection

from django.contrib.auth import login, authenticate, logout


def dictfetchall(cursor):
    "Return all rows from a cursor as a dict"
    columns = [col[0] for col in cursor.description]
    return [dict(zip(columns, row)) for row in cursor.fetchall()]


def fetch_students():
    students = connection.cursor()
    students.cursor.execute(
        """SELECT a.root, s.student_id, a.photo, u.first_name, u.last_name, s.current_year, s.major, a.gender, a.address, a.date_of_birth, a.phone, u.email, s.status
            FROM accounts_CustomUser u
            INNER JOIN accounts_UserAttributes a ON CAST(a.root AS INT) = u.id
            LEFT JOIN accounts_Student s ON s.root = u.id
            WHERE u.user_type = 'student'
            Order By u.id Desc
        """
    )
    return dictfetchall(students)


def fetch_notifications(user_id):
    notifications = connection.cursor()
    notifications.cursor.execute(
        """SELECT  an.date, an.notification_title, an.notification_rating, an.notify_class, an.assignment, sc.student_class
            FROM students_StudentClass sc
            INNER JOIN lecturers_AssignmentNotification an ON sc.student_class = an.notify_class
            WHERE sc.root =  %s
        """,
        [user_id],
    )
    notification_list = dictfetchall(notifications)
    total_notifications = len(notification_list)
    return notification_list, total_notifications


def fetch_lessons(user_id):
    lesson_allocation = connection.cursor()
    lesson_allocation.cursor.execute(
        """SELECT la.student_root, la.course, ol.online_title, ol.lesson_date, ol.lesson_start_time, ol.lesson_end_time, la.lecturer, ol.online_platform_link
            FROM classes_LessonAllocation la
            INNER JOIN classes_OnlineLesson ol ON ol.course_name = la.course
            WHERE la.student_root = %s
            Order By la.id Desc
        """,
        [user_id],
    )
    lesson_allocation = dictfetchall(lesson_allocation)
    total_lesson_allocations = len(lesson_allocation)
    return lesson_allocation, total_lesson_allocations
