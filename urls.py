from django.conf.urls.defaults import *
from blog.models import Blog

handler500 = 'djangotoolbox.errorviews.server_error'

urlpatterns = patterns('',
    ('^_ah/warmup$', 'djangoappengine.views.warmup'),
    ('^$', 'django.views.generic.simple.direct_to_template', {'template': 'home.html'}),
    (r'^/$', 'django.views.generic.simple.direct_to_template', {'template': 'home.html'}),
)

urlpatterns += patterns('blog.views',
    url(r'^(?P<username>\w+)/?$', 'list_blogs', {'public_only_flag' : True}, name="list_public_blogs"),
    url(r'^(?P<username>\w+)/admin/?$', 'list_blogs', {'public_only_flag' : False}, name="list_all_blogs"),
    url(r'^(?P<username>\w+)/(?P<blog_id>\d+)/?$', 'view_blog', name="view_blog"),
    url(r'^(?P<username>\w+)/(?P<blog_id>\d+)/edit/?$', 'edit_blog', name="edit_blog")
)
