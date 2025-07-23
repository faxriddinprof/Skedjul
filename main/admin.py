from django.contrib import admin
from .models import DailyExpense

@admin.register(DailyExpense)
class DailyExpenseAdmin(admin.ModelAdmin):
    list_display = ('date', 'ovqat', 'transport', 'salomatlik', 'boshqa', 'total_sum')
    search_fields = ('izoh',)
    list_filter = ('date',)
