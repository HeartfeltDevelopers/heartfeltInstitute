from django.contrib import admin
from .models import LendingBook, Stock


# Register your models here.


class StockAdmin(admin.ModelAdmin):
    list_display = ('book_id', 'book_title', 'book_lender', 'book_author')


admin.site.register(Stock, StockAdmin)


class LendingBookAdmin(admin.ModelAdmin):
    list_display = ('book', 'lending_date', 'return_date', 'student_borrower', 'availability', 'lender')


admin.site.register(LendingBook, LendingBookAdmin)
