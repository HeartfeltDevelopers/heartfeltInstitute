from django.db import models
from accounts.models import Student, Lecturer, Aluminum
from accounts.utilities import generate_book_id


class Stock(models.Model):
    book_id = models.CharField(max_length=20, unique=True, default=generate_book_id())
    book_title = models.CharField(max_length=250)
    book_description = models.TextField(blank=True)
    book_price = models.DecimalField(max_digits=8, decimal_places=2)
    book_author = models.CharField(max_length=500)
    book_lender = models.ForeignKey(Lecturer, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.book_id}, {self.book_title}, {self.book_author}'


class LendingBook(models.Model):
    book = models.ForeignKey(Stock, on_delete=models.SET_NULL, null=True)
    lending_date = models.DateTimeField()
    return_date = models.DateTimeField(null=True, blank=True)
    student_borrower = models.ForeignKey(Student, on_delete=models.CASCADE)
    lecturer_borrower = models.ForeignKey(Lecturer, on_delete=models.CASCADE)
    availability = models.BooleanField(default=True)
    lender = models.ForeignKey(Stock, on_delete=models.CASCADE, db_column='book_lender', related_name='book_lenders')

    def __str__(self):
        return (f'{self.book}, {self.lending_date}, {self.return_date}, {self.student_borrower},{self.availability}, '
                f'{self.lender}')


