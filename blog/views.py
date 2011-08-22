from django.shortcuts import get_object_or_404, render_to_response
from django.core.urlresolvers import reverse
from django.template import RequestContext, Context, loader
from blog.models import Blog
from django.http import Http404, HttpResponse, HttpResponseRedirect, HttpResponse
from django.conf.urls.defaults import *
from django.shortcuts import *

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
    if(POST):
        #loadform
        #make model
        #save model
        return render_to_response(  'blog/view_blog.html'
                                    ,{
                                        'blog': blog,
                                        'username':username
                                     }
                                    ,context_instance=RequestContext(request))
    else:
        if(blog_id is None): 
            blog = None
        else:
            blog = get_object_or_404(Blog, pk=blog_id)
        return render_to_response(  'blog/edit_blog.html'
                                    ,{
                                        'blog': blog,
                                        'username':username                                    
                                     }
                                    ,context_instance=RequestContext(request))


def delete_blog(request, username, blog_id):
    blog = get_object_or_404(Blog, pk=blog_id)
    blog.delete()
    return list_all_blogs(request, username)


def publish_blog(request, username, blog_id):
    blog = get_object_or_404(Blog, pk=blog_id)
    if (blog.publish is None): 
        blog.publish = datetime.now()
    else: 
        blog.publish = None
    blog.save()
    return render_to_response(  'blog/view_blog.html'
                                ,{
                                    'blog': blog,
                                    'username':username
                                 }
                                ,context_instance=RequestContext(request))



