from django.db import models
from django.urls import reverse
from django.core.exceptions import ValidationError
from django.utils import timezone
from django.conf import settings


KATEGORIYALAR = [
    ('ovqat', 'Ovqat'),
    ('transport', 'Transport'),
    ('salomatlik', 'Salomatlik'),
    ('boshqa', 'Boshqa'),
]

class DailyExpense(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True)
    date = models.DateField(default=timezone.now)
    ovqat = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    transport = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    salomatlik = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    boshqa = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    izoh = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.date} - Jami: {self.total_sum()}"

    def get_absolute_url(self):
        return reverse("home")

    def total_sum(self):
        return self.ovqat + self.transport + self.salomatlik + self.boshqa

    def clean(self):
        super().clean()
        if self.date < timezone.now().date():
            raise ValidationError({'date': "Sana bugungi kundan oldin bo'lishi mumkin emas."})

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
