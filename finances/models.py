from django.db import models
from accounts.models import Student, Partner, Lecturer


class Expense(models.Model):
    CATEGORY_CHOICES = [
        ('salary', 'Salary'),
        ('utilities', 'Utilities'),
        ('maintenance', 'Maintenance'),
        ('supplies', 'Supplies'),
        ('rent', 'Rent'),
        ('other', 'Other'),
    ]

    PAYMENT_METHOD_CHOICES = [
        ('cash', 'Cash'),
        ('mobile_money', 'Mobile Money'),
        ('bank_transfer', 'Bank Transfer'),
    ]

    category = models.CharField(max_length=100, choices=CATEGORY_CHOICES)
    description = models.CharField(max_length=200)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    payed_by = models.ForeignKey(Lecturer, on_delete=models.PROTECT, null=True, blank=True)
    date = models.DateField()
    payment_method = models.CharField(max_length=50, null=True, blank=True, choices=PAYMENT_METHOD_CHOICES)
    receipt_number = models.CharField(max_length=50, unique=True, null=True, blank=True)
    vendor = models.CharField(max_length=100, null=True, blank=True)
    notes = models.TextField(null=True, blank=True)
    is_approved = models.BooleanField(default=False)

    def __str__(self):
        return self.description


class Partnership(models.Model):
    partner = models.ForeignKey(Partner, on_delete=models.CASCADE)
    donation_type = models.CharField(max_length=10, choices=Partner.partner_type_choices)
    purpose = models.CharField(max_length=100)
    partnership_date = models.DateField()
    partnered_amount = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    food_items = models.TextField(null=True, blank=True)
    physical_items = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"Partnership by {self.partner}"
