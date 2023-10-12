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
            INNER JOIN accounts_Student s ON s.root = u.id
            WHERE u.user_type = 'student'
            Order By u.id Desc
        """
    )
    return dictfetchall(students)


def fetch_notifications(className):
    notifications = connection.cursor()
    notifications.cursor.execute(
        """SELECT  an.date, an.notification_title, an.notification_rating, an.notify_class, an.assignment
            FROM lecturers_AssignmentNotification an 
            WHERE an.notify_class = %s
        """,
        [className],
    )
    notification_list = dictfetchall(notifications)
    total_notifications = len(notification_list)
    return notification_list, total_notifications


def fetch_lessons(user_id):
    lesson_allocation = connection.cursor()
    lesson_allocation.cursor.execute(
        """SELECT  ol.course_name, ol.online_title, ol.lesson_date, ol.lesson_start_time, ol.lesson_end_time, ol.lecturer, ol.online_platform_link
            FROM classes_OnlineLesson ol 
            WHERE ol.course_name = %s
            Order By ol.id Desc
        """,
        [user_id],
    )
    lesson_allocation = dictfetchall(lesson_allocation)
    total_lesson_allocations = len(lesson_allocation)
    return lesson_allocation, total_lesson_allocations
