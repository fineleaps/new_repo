from django.conf.urls import url
from django.urls import path
from . import views
from django.contrib.auth.views import LoginView, LogoutView, logout_then_login

app_name = "portal"

urlpatterns = [
    url(r'^login/$', LoginView.as_view(template_name='portal/login.html'), name='login'),
    url(r'^logout/$', logout_then_login, name='logout'),
    # url(r'^$', views.HomeView.as_view(), name='home'),

    url(r'^$', views.home, name='home'),

    url(r'^profile/$', views.ProfileView.as_view(), name='profile'),
    url(r'^profile/update/$', views.ProfileUpdateView.as_view(), name='profile_update'),

    url(r"^password/change/$", views.password_change, name='password_change'),

]