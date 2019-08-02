from django.contrib.auth.mixins import UserPassesTestMixin
from django.views.generic import View
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DeleteView, UpdateView, FormView, DetailView, CreateView
from campaigns.models import Campaign, ProspectCampaignRelation
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from . import alert_messages
from django.contrib import messages
from .forms import CampaignUpdateForm, CampaignAddForm, ClientAddForm, ClientUpdateForm, CustomUserCreationForm
from clients.models import Client
from prospects.models import Prospect
from .filters import ProspectFilter, ResultFilter
from django_filters.views import FilterView
from portal.models import User


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
    success_url = reverse_lazy("crm_admin:campaign_list")

    # def get_success_url(self):
    #     campaign = self.get_object()
    #     return campaign.get_admin_update_url

    def form_valid(self, form):
        messages.success(self.request, alert_messages.CAMPAIGN_UPDATED_MESSAGE)
        return super().form_valid(form)


@superuser_required()
class CampaignAddView(LoginRequiredMixin, CreateView):

    model = Campaign
    form_class = CampaignAddForm
    template_name = "crm_admin/campaigns/add.html"
    success_url = reverse_lazy("crm_admin:campaign_list")

    # def get_success_url(self):
    #     campaign = self.get_object()
    #     return campaign.get_admin_update_url

    def form_valid(self, form):
        messages.success(self.request, alert_messages.CAMPAIGN_ADDED_MESSAGE)
        return super().form_valid(form)


@superuser_required()
class CampaignDeleteView(LoginRequiredMixin, DeleteView):

    model = Campaign
    template_name = "crm_admin/campaigns/delete.html"
    context_object_name = "campaign"
    success_url = reverse_lazy("crm_admin:campaign_list")

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, alert_messages.CAMPAIGN_DELETED_MESSAGE)
        return super().delete(self, request, *args, **kwargs)



@superuser_required()
class ClientListView(LoginRequiredMixin, ListView):

    model = Client
    template_name = "crm_admin/clients/list.html"
    context_object_name = "clients"


@superuser_required()
class ClientDetailView(LoginRequiredMixin, DetailView):

    model = Client
    template_name = "crm_admin/clients/detail.html"
    context_object_name = "client"


@superuser_required()
class ClientUpdateView(LoginRequiredMixin, UpdateView):

    model = Client
    form_class = ClientUpdateForm
    template_name = "crm_admin/clients/update.html"
    success_url = reverse_lazy("crm_admin:client_list")

    # def get_success_url(self):
    #     client = self.get_object()
    #     return client.get_admin_update_url

    def form_valid(self, form):
        messages.success(self.request, alert_messages.CAMPAIGN_UPDATED_MESSAGE)
        return super().form_valid(form)


@superuser_required()
class ClientAddView(LoginRequiredMixin, CreateView):

    model = Client
    form_class = ClientAddForm
    template_name = "crm_admin/clients/add.html"
    success_url = reverse_lazy("crm_admin:home")

    # def get_success_url(self):
    #     client = self.get_object()
    #     return client.get_admin_update_url

    def get_object(self, queryset=None):
        client = self.get_object()
        return client

    def form_valid(self, form):
        messages.success(self.request, alert_messages.CLIENT_ADDED_MESSAGE)
        return super().form_valid(form)


@superuser_required()
class ClientDeleteView(LoginRequiredMixin, DeleteView):

    model = Client
    template_name = "crm_admin/clients/delete.html"
    context_object_name = "client"
    success_url = reverse_lazy("crm_admin:client_list")

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, alert_messages.CLIENT_DELETED_MESSAGE)
        return super().delete(self, request, *args, **kwargs)


@superuser_required()
class ProspectListView(LoginRequiredMixin, ListView):

    model = Prospect
    template_name = "crm_admin/prospects/list.html"
    context_object_name = "prospects"


@superuser_required()
class ProspectListFilterView(LoginRequiredMixin, FilterView):

    filterset_class = ProspectFilter
    template_name = "crm_admin/prospects/list_filter.html"
    context_object_name = "prospects"


@superuser_required()
class ExecutiveListView(LoginRequiredMixin, ListView):

    model = User
    template_name = "crm_admin/executives/list.html"
    context_object_name = "executives"

    def get_queryset(self):
        qs = super().get_queryset().filter(is_staff=False, is_superuser=False)
        return qs


@superuser_required()
class ExecutiveUpdateView(LoginRequiredMixin, UpdateView):

    model = User
    template_name = "crm_admin/executives/update.html"
    context_object_name = "executive"
    fields = ("first_name", "last_name", "email", "phone", "employee_id", "date_of_birth", "details")
    success_url = reverse_lazy("crm_admin:executive_list")

    slug_field = "id"
    slug_url_kwarg = "id"

    def form_valid(self, form):
        messages.success(self.request, alert_messages.EXECUTIVE_UPDATED_MESSAGE)
        return super().form_valid(form)


@superuser_required()
class ExecutiveDeleteView(LoginRequiredMixin, DeleteView):

    model = User
    template_name = "crm_admin/executives/delete.html"
    context_object_name = "executive"
    success_url = reverse_lazy("crm_admin:executive_list")
    slug_field = "id"
    slug_url_kwarg = "id"

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, alert_messages.EXECUTIVE_DELETED_MESSAGE)
        return super().delete(self, request, *args, **kwargs)


@superuser_required()
class ProgressFilterView(LoginRequiredMixin, FilterView):

    filterset_class = ResultFilter
    template_name = 'crm_admin/progress/progress.html'


class ExecutiveAddView(CreateView):

    form_class = CustomUserCreationForm
    model = User
    template_name = "crm_admin/executives/add.html"
    success_url = reverse_lazy("crm_admin:executive_list")

    def form_valid(self, form):
        messages.success(self.request, alert_messages.EXECUTIVE_ADDED_MESSAGE)
        return super().form_valid(form)
