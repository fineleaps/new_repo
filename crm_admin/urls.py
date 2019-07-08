from django.conf.urls import url
from django.urls import path
from . import views
from django.contrib.auth.views import LoginView, LogoutView, logout_then_login


app_name = "crm_admin"

urlpatterns = [

    url(r'^$', views.HomeView.as_view(), name="home"),
    url(r'^campaigns/list/$', views.CampaignListView.as_view(), name='campagin_list'),
    url(r'^campaigns/add/$', views.CampaignAddView.as_view(), name='campaign_add'),
    url(r'^campaign/detail/(?P<slug>[-\w]+)/$', views.CampaignDetailView.as_view(), name="campaign_detail"),
    url(r'^campaign/update/(?P<slug>[-\w]+)/$', views.CampaignUpdateView.as_view(), name="campaign_update"),

    # url(r'^campaign/list/$', views.CampaignListView.as_view(), name='campaign_list'),
    # path('campaign/detail/<int:pk>/', views.CampaignDetailView.as_view(), name='campaign_detail'),

]