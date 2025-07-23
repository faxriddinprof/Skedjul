from django.shortcuts import render
from .forms import CustomUserCreationForm
from django.urls import reverse_lazy 
from django.contrib import messages  #  Messages import qilindi
from django.contrib.auth.views import LogoutView as DjangoLogoutView, LoginView
from django.views.generic.edit import FormView  
from django.contrib.auth.forms import AuthenticationForm


# Custom signup view
class SignupView(FormView):
    form_class = CustomUserCreationForm
    template_name = 'registration/signup.html'  
    success_url = reverse_lazy('login')
   
    def form_valid(self, form):
        messages.success(self.request, "✅ Muvaffaqiyatli ro'yxatdan o'tdingiz! Endi tizimga kiring.")
        return super().form_valid(form)


# Custom login view
class CustomLoginView(LoginView):
    template_name = 'registration/login.html'  # Siz yaratadigan HTML fayl
    authentication_form = AuthenticationForm
    next_page = reverse_lazy('home')  # Muvaffaqiyatli login bo‘lgach redirect qayerga bo‘lsin

    def form_invalid(self, form):
        messages.error(self.request, "Login muvaffaqiyatsiz. Login yoki parol noto‘g‘ri.")
        return super().form_invalid(form)
    
    def form_valid(self, form):
        messages.success(self.request, "✅ Siz tizimga muvaffaqiyatli kirdingiz !")
        return super().form_valid(form)
# Custom logout view
class LogoutView(DjangoLogoutView):
    def dispatch(self, request, *args, **kwargs):
        messages.success(request, "👋 Tizimdan chiqdingiz. Qaytib kelishingizni kutamiz!")
        return super().dispatch(request, *args, **kwargs)
    