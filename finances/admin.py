from django.contrib import admin
from .models import Expense, Fee, Partnership


class ExpenseAdmin(admin.ModelAdmin):
    list_display = ['category', 'description', 'amount', 'date', 'payment_method', 'receipt_number', 'vendor', 'notes',
                    'is_approved']
    search_fields = ['category', 'description', 'vendor']
    list_filter = ['category', 'date', 'is_approved']


admin.site.register(Expense, ExpenseAdmin)


class FeeAdmin(admin.ModelAdmin):
    list_display = ['student', 'fee_type', 'amount', 'semester', 'is_fully_paid', 'owing', 'payment_method',
                    'transaction_reference']
    search_fields = ['student__first_name', 'student__last_name', 'fee_type']
    list_filter = ['fee_type', 'semester', 'is_fully_paid', 'payment_method']


admin.site.register(Fee, FeeAdmin)


class PartnershipAdmin(admin.ModelAdmin):
    list_display = ['partner', 'partnership_date', 'partnered_amount', 'food_items', 'physical_items', 'donation_type']
    search_fields = ['partner', 'partnership_date', 'donation_type']
    list_filter = ['donation_type']


admin.site.register(Partnership, PartnershipAdmin)
