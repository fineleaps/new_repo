from django.shortcuts import render, redirect
from django.contrib.auth.mixins import UserPassesTestMixin
from django.views.generic import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DeleteView, UpdateView, FormView, DetailView, CreateView
from campaigns.models import Campaign, ProspectCampaignRelation
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import Http404
from results.forms import ResultAddForm
from django.urls import reverse_lazy
from . import alert_messages
from django.contrib import messages
from .forms import CampaignUpdateForm, CampaignAddForm


def superuser_required():
    def wrapper(wrapped):
        class WrappedClass(UserPassesTestMixin, wrapped):
            def test_func(self):
                return self.request.user.is_superuser

        return WrappedClass
    return wrapper


@superuser_required()
class HomeView(LoginRequiredMixin, View):
    def get(self, request):
        if request.user.is_superuser:
            return render(request, 'crm_admin/home.html')
        else:
            return redirect('portal:home')


@superuser_required()
class CampaignListView(LoginRequiredMixin, ListView):

    model = Campaign
    template_name = "crm_admin/campaigns/list.html"
    context_object_name = "campaigns"


@superuser_required()
class CampaignDetailView(LoginRequiredMixin, DetailView):

    model = Campaign
    template_name = "campaigns/detail.html"
    context_object_name = "campaign"


@superuser_required()
class CampaignUpdateView(LoginRequiredMixin, UpdateView):

    model = Campaign
    form_class = CampaignUpdateForm
    template_name = "crm_admin/campaigns/update.html"
    success_url = reverse_lazy("crm_admin:home")

    def get_success_url(self):
        campaign = self.get_object()
        return campaign.get_admin_update_url

    def form_valid(self, form):
        messages.success(self.request, alert_messages.CAMPAIGN_UPDATED_MESSAGE)
        return super().form_valid(form)


@superuser_required()
class CampaignAddView(LoginRequiredMixin, CreateView):

    model = Campaign
    form_class = CampaignAddForm
    template_name = "crm_admin/campaigns/add.html"

    def get_success_url(self):
        campaign = self.get_object()
        return campaign.get_admin_update_url

    def form_valid(self, form):
        messages.success(self.request, alert_messages.CAMPAIGN_ADDED_MESSAGE)
        return super().form_valid(form)


@superuser_required()
class CampaignDetailView(LoginRequiredMixin, DeleteView):

    model = Campaign
    template_name = "crm_admin/campaigns/delete.html"
    context_object_name = "campaign"

