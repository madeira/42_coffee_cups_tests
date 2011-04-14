from django.conf.urls.defaults import *
from django.conf import settings
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    (r'^admin/', include(admin.site.urls)),
    url(r'^edit/', "contact.views.edit_person", name="contact_edit"),
    url(r'^accounts/login/$', 'django.contrib.auth.views.login',
        {'template_name': 'login.html'}, name='login'),
    url(r'^logout/$', 'django.contrib.auth.views.logout',
        {'next_page': '/'}, name='logout'),
    url(r'^$', "contact.views.show_person", name='home'),
    url(r'^request/$', "requestlog.views.request_list", name='requestlog'),
    url(r'^processor/$', "mysite.views.show_settings", name='processor'),
    url(r'^request/filter/(?P<offset>\w+)/$',
        "requestlog.views.request_true_false_priority",
        name='requestlog_filter'),
    url(r'^request/sorting/(?P<offset>\w+)/$',
        "requestlog.views.request_asc_desc_priority",
        name='requestlog_sorting'),
)
if settings.DEBUG == True:
    urlpatterns += patterns('', (r'^%s(?P<path>.*)$' % settings.MEDIA_URL,
                                 'django.views.static.serve',
                                 {'document_root': settings.MEDIA_ROOT}), )
