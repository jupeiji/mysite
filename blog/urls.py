from django.urls import path
from .import views
app_name = 'blog'

urlpatterns = [
    #http://localhost:8000/blog/
    path('<int:blog_pk>',views.blog_detail,name = 'blog_detail'),
    path('',views.blog_list,name = 'blog_list'),
    ]