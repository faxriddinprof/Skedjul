from django.urls import path
from .views import (
    Homepageview,
    BlogCreateview,
    BlogDetailview, 
    BlogUpdateview,
    BlogDeleteview,

)

urlpatterns=[
    path('', Homepageview.as_view(), name='home'),
    path('post/new/', BlogCreateview.as_view(), name='post_create'),
    path('post/<int:pk>/', BlogDetailview.as_view(), name='post_detail'),
    path('post/<int:pk>/edit/', BlogUpdateview.as_view(), name='post_update'),
    path('post/<int:pk>/delete/', BlogDeleteview.as_view(), name='post_delete'),

]