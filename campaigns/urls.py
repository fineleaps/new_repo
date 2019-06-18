from django.conf.urls import url
from django.urls import path
from . import views
from django.contrib.auth.views import LoginView, LogoutView, logout_then_login


app_name = "campaigns"

urlpatterns = [

    url(r'^list/$', views.CampaignListView.as_view(), name='list'),
    url(r'^detail/(?P<slug>[-\w]+)/$', views.CampaignDetailView.as_view(), name="detail"),
    url(r'^prospect/get/(?P<slug>[-\w]+)/$', views.prospect_get, name="prospect_get"),


    # url('(?P<slug>[-\w]+)/(?P<pk>\d+)/$', views.posts, name='posts'),

    # path('campaign/detail/<slug:slug>/', views.CampaignDetailView.as_view(), name='detail'),

]
