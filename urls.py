from django.conf.urls.defaults import *
from django.views.generic import DetailView, ListView
from blog.models import Blog

handler500 = 'djangotoolbox.errorviews.server_error'

urlpatterns = patterns('',
    ('^_ah/warmup$', 'djangoappengine.views.warmup'),
    ('^$', 'django.views.generic.simple.direct_to_template', {'template': 'home.html'}),
    (r'^/$', 'django.views.generic.simple.direct_to_template', {'template': 'home.html'}),
    (r'^/', include('blog.urls')),
)

