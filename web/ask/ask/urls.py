from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
#	url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'qa.views.question_list', name='question_list'),
    url(r'^login/', 'qa.views.test'),
    url(r'^signup', 'qa.views.test'),
    url(r'^question/(?P<pk>\d+)', 'qa.views.question_detail', name='question_detail'),
    url(r'^ask/', 'qa.views.test', name='test'),
    url(r'^popular/', 'qa.views.popular', name='popular'),
    url(r'^new', 'qa.views.test'),
#    url(r'^answer/$', 'qa.views.answer', name='answer'),
)