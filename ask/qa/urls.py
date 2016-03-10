from django.conf.urls import patterns, include, url

urlpatterns = patterns('qa.views',
url(r'^$', 'question_new', name='question_new'),
    url(r'^ask/', 'test', name='ask'),
    url(r'^login/', 'test', name='login'),
    url(r'^new/', 'test', name='new'),
    url(r'^popular/', 'test', name='popular'),
    url(r'^signup/', 'test', name='signup'),
    url(r'^question/(\d+)/$', 'question_details', name='question_details'),
)
