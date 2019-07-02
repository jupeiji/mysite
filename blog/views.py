from django.shortcuts import render_to_response,get_object_or_404
from .models import Blog
from datetime import datetime

# Create your views here.
def blog_list(request):
    context = {}
    context['blogs'] = Blog.objects.all()
    #context['blog_count'] = Blog.objects.all().count() //另一种统计博客数量的方法
    return render_to_response('blog_list.html',context)
def blog_detail(request,blog_pk):
    blog = get_object_or_404(Blog,pk = blog_pk)
    if not request.COOKIES.get('blog_%s_readed' % blog_pk):
        blog.readed_num += 1
        blog.save()
    context = {}
    context['blog'] = get_object_or_404(Blog,pk = blog_pk)
    response =  render_to_response('blog_detail.html',context)
    response.set_cookie('blog_%s_readed' % blog_pk,'true')
    return response

