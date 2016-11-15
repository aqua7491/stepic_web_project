from django.conf.urls import url
from qa.views import test, question_list, question_detail, popular
#from qa.views import question_ask, question_answer
#from qa.views import user_signup, user_login, user_logout

urlpatterns = [
    url(r'^$', question_list, name='question_list'),
    url(r'^popular/$', popular, name='popular'),
    url(r'^question/(?P<pk>\d+)/$', question_detail, name='question_detail')
    url(r'^login/$', test, name='test'),
    url(r'^signup/$', test,name='test'),
    url(r'^ask/.*$', test,name='test'),
    url(r'^new/$', test,name='test'),
]



