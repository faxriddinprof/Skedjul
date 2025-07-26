from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import View
from datetime import date
from django.shortcuts import render
from .analytics import (
    get_category_totals, get_time_series, get_monthly_yearly_summary,
    get_top_spend, get_percentage_contribution, get_forecast
)
from main.models import DailyExpense

class StatisticsView(LoginRequiredMixin, View):
    def get(self, request):
        user = request.user
        year = request.GET.get('year')
        if year:
            try:
                year = int(year)
            except ValueError:
                year = date.today().year
        else:
            year = date.today().year

        # Barcha mavjud yillar ro'yxati (eng yangi eng oldinda)
        all_years = DailyExpense.objects.filter(user=user).order_by('-year').values_list('year', flat=True).distinct()

        # Statistikalar
        cat_totals = get_category_totals(user, year)
        months, time_series = get_time_series(user, year)
        summary = get_monthly_yearly_summary(user, year)
        top_day, top_month = get_top_spend(user, year)
        perc = get_percentage_contribution(cat_totals)
        forecast_month, forecast_year = get_forecast(user, year)

        context = {
            'selected_year': year,
            'all_years': all_years,  # 👈 dropdown uchun kerak
            'cat_totals': cat_totals,
            'cat_labels': list(cat_totals.keys()),
            'cat_data': [float(v) for v in cat_totals.values()],
            'months': summary['months'],
            'time_series': [float(x) for x in time_series],
            'monthly_sum': summary['monthly_sum'],
            'avg_monthly': summary['avg_monthly'],
            'yearly_sum': summary['yearly_sum'],
            'avg_yearly': summary['avg_yearly'],
            'top_day': top_day,
            'top_month': top_month,
            'perc': perc,
            'forecast_month': forecast_month,
            'forecast_year': forecast_year,
        }

        return render(request, 'statisticpage/statistics.html', context)
