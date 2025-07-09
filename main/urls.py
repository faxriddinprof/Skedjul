from django.urls import path
from .views import (
    Homepageview,
    BlogCreateview,
    BlogDetailview, 
    BlogUpdateview,
    BlogDeleteview,
    update_status_ajax,
    update_post_ajax,
    delete_post_ajax,

)

urlpatterns=[
    path('', Homepageview.as_view(), name='home'),
    path('post/new/', BlogCreateview.as_view(), name='post_create'),
    path('post/<int:pk>/', BlogDetailview.as_view(), name='post_detail'),
    path('update-status/<int:pk>/', update_status_ajax, name='update_status_ajax'),
    path('update-post/<int:pk>/', update_post_ajax, name='update_post_ajax'),
    path('delete-post/<int:pk>/', delete_post_ajax, name='delete_post_ajax'),



]