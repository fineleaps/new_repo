from django.conf.urls import url
from django.urls import path
from . import views
from django.contrib.auth.views import LoginView, LogoutView, logout_then_login

app_name = "portal"

urlpatterns = [
    url(r'^login/$', LoginView.as_view(template_name='portal/login.html'), name='login'),
    url(r'^logout/$', logout_then_login, name='logout'),
    url(r'^$', views.HomeView.as_view(), name='home'),

    url(r'^profile/$', views.ProfileView.as_view(), name='profile'),

]