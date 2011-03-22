from django.conf.urls.defaults import *
from django.conf import settings
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    (r'^admin/', include(admin.site.urls)),
    (r'^edit/', "contact.views.edit_person"),
    url(r'^accounts/login/$', 'django.contrib.auth.views.login', {'template_name': 'login.html'}),
    url(r'^logout/$', 'django.contrib.auth.views.logout', {'next_page': '/'}),
    (r'^$', "contact.views.show_person"),
    (r'^request/$', "requestlog.views.request_list"),
    (r'^processor/$', "mysite.views.show_settings"),
)
if settings.DEBUG == True:
    urlpatterns += patterns('', (r'^%s(?P<path>.*)$' % settings.MEDIA_URL,
                                 'django.views.static.serve',
                                 {'document_root': settings.MEDIA_ROOT}), )
