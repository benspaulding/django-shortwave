from django.conf.urls.defaults import *


urlpatterns = patterns('',
    (r'^shortwave/', include('shortwave.urls')),
)
