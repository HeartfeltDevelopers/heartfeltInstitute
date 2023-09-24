import random
import datetime


def generate_student_id():
    random_number = random.randint(10000000, 99999999)
    today = datetime.date.today()
    year = today.strftime("%Y")
    return f'HIM-{random_number}-{year}'


def generate_employee_number():
    random_number = random.randint(100000, 999999)
    today = datetime.date.today()
    year = today.strftime("%Y")
    return f'HIM-LEC-{random_number}'


def generate_partner_number():
    random_number = random.randint(100000, 999999)
    today = datetime.date.today()
    year = today.strftime("%Y")
    return f'HIM-PTR-{random_number}-{year}'


def generate_library_number():
    random_number = random.randint(10000, 99999)
    today = datetime.date.today()
    year = today.strftime("%Y")
    return f'LBY-{random_number}-{year}'

def generate_course_number():
    random_number = random.randint(1000, 9999)
    today = datetime.date.today()
    year = today.strftime("%Y")
    return f'CRS-{random_number}-{year}'

def generate_book_id():
    random_number = random.randint(1000, 9999)
    today = datetime.date.today()
    year = today.strftime("%Y")
    return f'BOOK-{random_number}-{year}'


