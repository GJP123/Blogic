from django.conf.urls.defaults import *
from blog.models import Blog

handler500 = 'djangotoolbox.errorviews.server_error'

urlpatterns = patterns('',
    ('^_ah/warmup$', 'djangoappengine.views.warmup'),
)

urlpatterns += patterns('blog.views',
    url(r'^/?$', 'list_public_blogs', {'username': 'graham'}, name="list_public_blogs"),
    url(r'^(?P<username>\w+)/?$', 'list_public_blogs', name="list_public_blogs"),
    url(r'^(?P<username>\w+)/public/?$', 'list_public_blogs', name="list_public_blogs"),
    url(r'^(?P<username>\w+)/all/?$', 'list_all_blogs', name="list_all_blogs"),
    url(r'^(?P<username>\w+)/(?P<blog_id>\d+)/?$', 'view_blog', name="view_blog"),
    url(r'^(?P<username>\w+)/(?P<blog_id>\d+)/edit/?$', 'edit_blog', name="edit_blog"),
    url(r'^(?P<username>\w+)/new/?$', 'edit_blog', {'blog_id': None},  name="new_blog"), #send 'new' requests to the 'edit' view 
    url(r'^(?P<username>\w+)/(?P<blog_id>\d+)/publish/?$', 'publish_blog', name="publish_blog"),
    url(r'^(?P<username>\w+)/(?P<blog_id>\d+)/delete/?$', 'delete_blog', name="delete_blog"),
)
