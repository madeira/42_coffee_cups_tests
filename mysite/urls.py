from django.conf.urls.defaults import *
from django.conf import settings
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    (r'^admin/', include(admin.site.urls)),
)
if settings.DEBUG == True:
    urlpatterns += patterns('', (r'^%s(?P<path>.*)$' % settings.MEDIA_URL,
         'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}), )
