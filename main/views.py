from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.urls import reverse_lazy
from .models import Post
from .forms import DateInput, PromiseForm
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.http import HttpResponseRedirect
# Create your views here.


class Homepageview(ListView):
    model = Post
    template_name = "home.html"


class BlogCreateview(CreateView):
    model = Post
    form_class=PromiseForm
    template_name='post_create.html'
    success_url=reverse_lazy('home')

class BlogDetailview(DetailView):
    model=Post
    template_name='post_detail.html'

class BlogUpdateview(UpdateView):
    model=Post
    template_name='post_update.html'
    fields=['title','text']
    success_url=reverse_lazy('home')

class BlogDeleteview(DeleteView):
    model=Post
    success_url=reverse_lazy('home')


    def get(self, request, *args, **kwargs):
        return HttpResponseRedirect(self.get_object().get_absolute_url())
#-----------------------change------------------------------------------------

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Post
import json

@csrf_exempt
def update_status_ajax(request, pk):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            post = Post.objects.get(pk=pk)
            post.holati = data['status'] == 'true'
            post.save()
            return JsonResponse({'success': True, 'new_status': post.holati})
        except Post.DoesNotExist:
            return JsonResponse({'success': False, 'error': 'Topilmadi'})
    return JsonResponse({'success': False, 'error': 'Notog‘ri so‘rov'})



from datetime import date

@csrf_exempt
def update_post_ajax(request, pk):
    if request.method == 'POST':
        try:
            post = Post.objects.get(pk=pk)
            data = json.loads(request.body)

            # Sana validatsiyasi
            try:
                selected_date = date.fromisoformat(data['date'])
            except ValueError:
                return JsonResponse({'success': False, 'error': 'Noto‘g‘ri sana formati'})

            if selected_date < date.today():
                return JsonResponse({'success': False, 'error': 'Sana bugungi kundan oldin bo‘lishi mumkin emas'})

            # Yangilash
            post.title = data['title']
            post.text = data['text']
            post.date = selected_date
            post.save()
            return JsonResponse({'success': True})

        except Post.DoesNotExist:
            return JsonResponse({'success': False, 'error': 'Post topilmadi'})

    return JsonResponse({'success': False, 'error': 'Notog‘ri so‘rov'})


@csrf_exempt
def delete_post_ajax(request, pk):
    if request.method == 'POST':
        try:
            post = Post.objects.get(pk=pk)
            post.delete()
            return JsonResponse({'success': True})
        except Post.DoesNotExist:
            return JsonResponse({'success': False, 'error': 'Post topilmadi'})
    return JsonResponse({'success': False, 'error': 'Notog‘ri so‘rov'})
