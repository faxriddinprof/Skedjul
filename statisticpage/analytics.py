# bu kodlar statistikalar sahifasida ishlatiladigan funksiyalar



from datetime import date
import calendar
from django.db.models import Sum, F
from main.models import DailyExpense




# bu funksiya har bir tur harajatlar bo'yicha jami summani hisoblaydi
# masalan: ovqat, transport, salomatlik, boshqa

def get_category_totals(user):
    qs = DailyExpense.objects.filter(user=user)
    return {
        'ovqat': qs.aggregate(sum=Sum('ovqat'))['sum'] or 0,
        'transport': qs.aggregate(sum=Sum('transport'))['sum'] or 0,
        'salomatlik': qs.aggregate(sum=Sum('salomatlik'))['sum'] or 0,
        'boshqa': qs.aggregate(sum=Sum('boshqa'))['sum'] or 0,
    }

#Oy‐oy bo‘yicha joriy yilda harajatlar ro‘yxati (0 bo‘lsa ham)
# masalan: yanvar, fevral, mart va hokazo

def get_time_series(user):
    year = date.today().year
    # oy nomlari
    months = [calendar.month_abbr[m] for m in range(1,13)]
    data = {m:0 for m in range(1,13)}

    qs = DailyExpense.objects.filter(user=user, date__year=year)\
          .values_list('date__month')\
          .annotate(monthly=Sum(F('ovqat')+F('transport')+F('salomatlik')+F('boshqa')))
    
    # har bir oy uchun jami summani olish
    for month, total in qs:
        data[month] = total
    return months, [data[m] for m in range(1,13)]



def get_monthly_yearly_summary(user):
    # vaqt seriyali
    months, ts = get_time_series(user)
    monthly_sum = sum(ts)
    months_done = date.today().month
    avg_monthly = monthly_sum / months_done if months_done else 0

    # kunlik o'rtacha
    year_start = date(date.today().year,1,1)
    days_done = (date.today() - year_start).days + 1
    total_sum = sum(
        DailyExpense.objects.filter(user=user)
        .annotate(s=F('ovqat')+F('transport')+F('salomatlik')+F('boshqa'))
        .values_list('s', flat=True)
    )
    avg_daily = total_sum / days_done if days_done else 0
    avg_yearly = avg_daily * 365
    return {
        'months': months,
        'monthly_sum': monthly_sum,
        'avg_monthly': round(avg_monthly,2),
        'yearly_sum': total_sum,
        'avg_yearly': round(avg_yearly,2),
    }




# bu funksiya eng ko'p sarflangan kun va oylarni qaytaradi
# masalan: 2023-01-15, 2023-02-20
def get_top_spend(user):
    qs = DailyExpense.objects.filter(user=user)
    # kunlik
    by_day = qs.values('date')\
               .annotate(total=Sum(F('ovqat')+F('transport')+F('salomatlik')+F('boshqa')))\
               .order_by('-total')
    top_day = by_day.first()
    # oylik
    by_month = qs.values('date__month')\
                 .annotate(total=Sum(F('ovqat')+F('transport')+F('salomatlik')+F('boshqa')))\
                 .order_by('-total')
    top_month = by_month.first()
    if top_month:
        month_num = top_month['date__month']
        top_month['month_name'] = calendar.month_name[month_num]
    return top_day, top_month


# bu funksiya har bir tur xarajatning umumiy summasini hisoblaydi
# masalan: ovqat 30%, transport 20% va hokazo
def get_percentage_contribution(category_totals):
    total = sum(category_totals.values()) or 1
    return {k: round(v/total*100,2) for k,v in category_totals.items()}


# bu funksiya kelajakdagi taxminiy xarajatlarni hisoblaydi
# masalan: 2023 yil uchun 10000, 2024 yil uchun 12000
def get_forecast(user):
    qs = DailyExpense.objects.filter(user=user)
    days = qs.values_list('date', flat=True).distinct().count()
    total = sum([e.ovqat+e.transport+e.salomatlik+e.boshqa for e in qs])
    avg_daily = total/days if days else 0
    days_left = (date(date.today().year,12,31)-date.today()).days
    forecast_year = round(total + avg_daily*days_left,2)
    forecast_month = round(avg_daily * 30,2)
    return forecast_month, forecast_year

