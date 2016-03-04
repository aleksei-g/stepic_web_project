from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'ask.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^|ask/|login/|new/|popular/|singup/|question/<\d+>/', 'qa.views.test', name='test'),

    url(r'^admin/', include(admin.site.urls)),
)
