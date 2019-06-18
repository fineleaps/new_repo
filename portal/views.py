from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.views.generic import View, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Executive


class HomeView(LoginRequiredMixin, View):

    # def get(self, request):
    #     if request.user.is_superuser:
    #         return redirect('crm_admin:home')
    #     else:
    #         return render(request, 'portal/home.html')
    def get(self, request):
        return render(request, 'portal/home.html')


class ProfileView(LoginRequiredMixin, DetailView):

    template_name = "portal/profile.html"
    context_object_name = "executive"

    def get_object(self, queryset=None):
        return self.request.user.executive


#
# e
# @login_required
# def profile(request):
#
#     context = {"executive": }
#
#     return render(rquest, 'portal/profile.html', context)
#
