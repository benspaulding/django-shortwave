from django.conf.urls.defaults import *

from shortwave.views import wave_list, wave_detail


urlpatterns = patterns('',
    url(r'^$',
        wave_list,
        name='shortwave-wave-list',
    ),
    url(r'^(?P<username>[-\w]+)/$',
        wave_detail,
        name='shortwave-wave-detail',
    ),
)
