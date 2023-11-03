from django.db import models
from accounts.models import Student

# Create your models here.


class Program(models.Model):
    program_name = models.CharField(max_length=255, default='Diploma')
    description = models.TextField()
    year = models.PositiveIntegerField()
    
    def __str__(self):
        return self.program_name


class ProgramLevel(models.Model):
    name = models.CharField(max_length=255, default='Foundation')
    program = models.ForeignKey(Program, on_delete=models.CASCADE)


class Enrollment(models.Model):
    STATUS_CHOICES = (
        ('Active', 'Active'),
        ('Inactive', 'Inactive'),
    )

    program = models.ForeignKey('Program', on_delete=models.CASCADE)
    level = models.ForeignKey('ProgramLevel', on_delete=models.CASCADE)  
    student = models.ForeignKey(Student, on_delete=models.CASCADE)  
    status = models.CharField(max_length=50, choices=STATUS_CHOICES)
    start_date = models.DateField()  
    end_date = models.DateField()  
    
    def __str__(self):
        return f"{self.student} - {self.program} - {self.level}"



class Fees_Payment(models.Model):
    PAYMENT_CHOICES = (
        ('Credit Card', 'Credit Card'),
        ('Cash', 'Cash'),
        ('Transfer', 'Transfer'),
        ('Other', 'Other'),
    )

    
    FEES_TYPE = (
        ('fees', 'Fees'),
        ('levy', 'Levy'),
    )

    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    payment_type = models.CharField(max_length=50, choices=PAYMENT_CHOICES)
    payment_amount = models.DecimalField(max_digits=10, decimal_places=2)
    owing = models.DecimalField(max_digits=8, decimal_places=2)
    semester = models.CharField(max_length=20, choices=Student.CURRENT_CLASS)
    enrollment = models.ForeignKey('Enrollment', on_delete=models.CASCADE)  
    fee_type = models.CharField(max_length=10, choices=FEES_TYPE)
    is_fully_paid = models.BooleanField(default=False)
    date_paid = models.DateField() 
    transaction_reference = models.CharField(max_length=100, null=True, blank=True)
    
    def __str__(self):
        return f"{self.student} - {self.payment_type} - {self.payment_amount}"
    
