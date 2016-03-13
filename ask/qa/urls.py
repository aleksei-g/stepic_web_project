from django.conf.urls import patterns, include, url

urlpatterns = patterns('qa.views',
url(r'^$', 'question_new', name='question_new'),
    url(r'^ask/', 'question_add', name='question_add'),
    url(r'^login/', 'test', name='login'),
    url(r'^new/', 'test', name='new'),
    url(r'^popular/', 'question_popular', name='question_popular'),
    url(r'^signup/', 'test', name='signup'),
    url(r'^question/(\d+)/$', 'question_details', name='question_details'),
    url(r'^answer/(?P<question_id>\d+)/$', 'answer_add', name='answer_add'),
)
