from django.conf.urls import url
from django.urls import path
from . import views
from django.contrib.auth.views import LoginView, LogoutView, logout_then_login


app_name = "crm_admin"

urlpatterns = [

    url(r'^$', views.HomeView.as_view(), name="home"),
    url(r'^campaigns/list/$', views.CampaignListView.as_view(), name='campagin_list'),
    url(r'^campaigns/add/$', views.CampaignAddView.as_view(), name='campaign_add'),
    url(r'^campaigns/detail/(?P<slug>[-\w]+)/$', views.CampaignDetailView.as_view(), name="campaign_detail"),
    url(r'^campaigns/update/(?P<slug>[-\w]+)/$', views.CampaignUpdateView.as_view(), name="campaign_update"),
    url(r'^campaigns/delete/(?P<slug>[-\w]+)/$', views.CampaignDeleteView.as_view(), name="campaign_delete"),

    url(r'^clients/list/$', views.ClientListView.as_view(), name='client_list'),
    url(r'^clients/add/$', views.ClientAddView.as_view(), name='client_add'),
    url(r'^clients/detail/(?P<slug>[-\w]+)/$', views.ClientDetailView.as_view(), name="client_detail"),
    url(r'^clients/update/(?P<slug>[-\w]+)/$', views.ClientUpdateView.as_view(), name="client_update"),
    url(r'^clients/delete/(?P<slug>[-\w]+)/$', views.ClientDeleteView.as_view(), name="client_delete"),

    # url(r'^campaign/list/$', views.CampaignListView.as_view(), name='campaign_list'),
    # path('campaign/detail/<int:pk>/', views.CampaignDetailView.as_view(), name='campaign_detail'),

]