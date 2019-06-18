from django.conf.urls import url
from django.urls import path
from . import views
from django.contrib.auth.views import LoginView, LogoutView, logout_then_login

app_name = "prospects"

urlpatterns = [

    # url(r'^prospect/get/(?P<campaign_id>[0-9]+)$', views.prospect_get, name='prospect_get'),
    #
    #
    # url(r'^prospect/attempt_result/add/(?P<campaign_id>[0-9]+)/(?P<prospect_id>[0-9]+)/$',
    #     views.prospect_attempt_result_add, name='prospect_attempt_result_add'),

]