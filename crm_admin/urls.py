from django.conf.urls import url
from django.urls import path
from . import views
from django.contrib.auth.views import LoginView, LogoutView, logout_then_login


app_name = "crm_admin"

urlpatterns = [

    # url(r'^campaign/list/$', views.CampaignListView.as_view(), name='campaign_list'),
    # path('campaign/detail/<int:pk>/', views.CampaignDetailView.as_view(), name='campaign_detail'),

]