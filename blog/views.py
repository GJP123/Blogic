from django.shortcuts import get_object_or_404, render_to_response
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.template import RequestContext
from django.template import Context, loader
from blog.models import Blog
from django.http import Http404
from django.conf.urls.defaults import *
from django.http import HttpResponse
from django.shortcuts import *

def list_blogs(request, username, public_only_flag):
    blogs = Blog.objects.filter(username__exact=username)
    return render_to_response(  'blog/list_blogs.html'
                                ,{
                                    'blogs': blogs,
                                    'public_only_flag': published_flag,
                                    'username':username
                                 }
                                ,context_instance=RequestContext(request))


def view_blog(request, username, blog_id):
    blog = ''#get_object_or_404(Blog, pk=blog_id)
    return render_to_response(  'blog/view_blog.html'
                                ,{
                                    'blog': blog,
                                    'username':username
                                 }
                                ,context_instance=RequestContext(request))


def edit_blog(request, username, blog_id):
    blog = ''#get_object_or_404(Blog, pk=blog_id)
    return render_to_response(  'blog/edit_blog.html'
                                ,{
                                    'blog': blog,
                                    'username':username                                    
                                 }
                                ,context_instance=RequestContext(request))


def delete_blog(request, username, blog_id):
    blog = ''#get_object_or_404(Blog, pk=blog_id)
    #DELETE blog here
    list_blogs(request, username, false)