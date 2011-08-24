from django.shortcuts import get_object_or_404, render_to_response
from django.core.urlresolvers import reverse
from django.template import RequestContext, Context, loader
from blog.models import Blog, BlogForm
from django.http import Http404, HttpResponse, HttpResponseRedirect, HttpResponse
from django.conf.urls.defaults import *
from django.shortcuts import *
from datetime import *

def list_public_blogs(request, username):
    blogs = Blog.objects.filter(username__exact=username, published_date__isnull=False).order_by('-published_date')
    return render_to_response(  'blog/list_public_blogs.html'
                                ,{
                                    'blogs': blogs,
                                    'username':username
                                 }
                                ,context_instance=RequestContext(request))


def list_all_blogs(request, username):
    blogs = Blog.objects.filter(username__exact=username)
    return render_to_response(  'blog/list_all_blogs.html'
                                ,{
                                    'blogs': blogs,
                                    'username':username
                                 }
                                ,context_instance=RequestContext(request))


def view_blog(request, username, blog_id):
    blog = Blog.objects.get(pk=blog_id)
    return render_to_response(  'blog/view_blog.html'
                                ,{
                                    'blog': blog,
                                    'username':username
                                 }
                                ,context_instance=RequestContext(request))


def edit_blog(request, username, blog_id = None):
    if request.method == 'POST':        
        if blog_id is None:
            blog = Blog()
            blog.create_date = datetime.now() 
            blog.username = username   
        else:
            blog = Blog.objects.get(pk=blog_id)
        form = BlogForm(request.POST, instance=blog)
        if form.is_valid():          
            blog.modify_date = datetime.now() #every edit changed the modify date
            blog.published_date = None #since we have edited the blog we will need to re-publish it (maybe not the right thing to do)
            #import logging; logging.debug(form.instance.__dict__)
            form.save()                
            #import logging; logging.debug(form.instance.__dict__)
            return redirect('blog.views.view_blog', username=username, blog_id=blog.pk)
    else:
        if blog_id is None : 
            form = BlogForm()
        else:
            blog = get_object_or_404(Blog, pk=blog_id)
            form = BlogForm(instance=blog)

    return render_to_response(  'blog/edit_blog.html'
                                ,{
                                    'blog_id': blog_id,
                                    'form': form,
                                    'username':username,
                                 }
                                ,context_instance=RequestContext(request))

def delete_blog(request, username, blog_id):
    blog = get_object_or_404(Blog, pk=blog_id)
    blog.delete()
    return redirect('blog.views.list_all_blogs', username=username)


def publish_blog(request, username, blog_id):
    blog = get_object_or_404(Blog, pk=blog_id)
    if (blog.published_date is None): 
        blog.published_date = datetime.now()
    else: 
        blog.published_date = None
    blog.save()
    return redirect('blog.views.view_blog', username=username, blog_id=blog_id)



