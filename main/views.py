from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, View
from django.http import JsonResponse
from .models import DailyExpense
from .forms import DailyExpenseForm
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.contrib.auth.decorators import login_required

class DailyExpenseListView(LoginRequiredMixin,ListView):
    model = DailyExpense
    template_name = 'home.html'
    context_object_name = 'expenses'
    ordering = ['-date']  # oxirgi sana birinchi chiqadi

class DailyExpenseCreateView(CreateView):
    model = DailyExpense
    form_class = DailyExpenseForm
    template_name = 'add_expense.html'
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        messages.success(self.request, "✅ Xarajat muvaffaqiyatli qo'shildi!")
        return super().form_valid(form)


@csrf_exempt
def update_expense(request):
    if request.method == 'POST':
        expense_id = request.POST.get('id')
        expense = get_object_or_404(DailyExpense, id=expense_id)
        expense.date = request.POST.get('date')
        expense.ovqat = request.POST.get('ovqat') or 0
        expense.transport = request.POST.get('transport') or 0
        expense.salomatlik = request.POST.get('salomatlik') or 0
        expense.boshqa = request.POST.get('boshqa') or 0
        expense.izoh = request.POST.get('izoh')
        expense.save()
        messages.success(request, "✅ Xarajat muvaffaqiyatli yangilandi.")
        return redirect('/')  # Sahifani yangilaydi
    

@login_required
def delete_expense(request, pk):
    expense = get_object_or_404(DailyExpense, pk=pk)
    if request.method == 'POST':
        expense.delete()
        messages.success(request, "Xarajat muvaffaqiyatli o‘chirildi.")
        return redirect('home')  # o'zingizning bosh sahifa URL nomini qo'ying
    return redirect('home')