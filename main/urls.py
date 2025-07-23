from django.urls import path
from .views import (
    DailyExpenseListView,
    DailyExpenseCreateView,
    DeleteExpenseView,
    update_expense,
)

urlpatterns = [
    path('', DailyExpenseListView.as_view(), name='home'),  # Home sahifa – xarajatlar ro'yxati
    path('add/', DailyExpenseCreateView.as_view(), name='add_expense'),  # Xarajat qo'shish
    path('update/', update_expense , name='update_expense'),  # AJAX bilan update
    path('delete/<int:pk>/', DeleteExpenseView.as_view(), name='delete_expense'),  # AJAX bilan delete
]
