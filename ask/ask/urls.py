from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'ask.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    #url(r'^(|ask/|login/|new/|popular/|signup/|question/<\d+>/)$', 'qa.views.test', name='test'),
    url(r'^$', 'qa.views.test', name='ask'),
    url(r'^ask/', 'qa.views.test', name='ask'),
    url(r'^login/', 'qa.views.test', name='login'),
    url(r'^new/', 'qa.views.test', name='new'),
    url(r'^popular/', 'qa.views.test', name='popular'),
    url(r'^signup/', 'qa.views.test', name='signup'),
    url(r'^question/<\d+>/', 'qa.views.test', name='question'),

    url(r'^admin/', include(admin.site.urls)),
)
