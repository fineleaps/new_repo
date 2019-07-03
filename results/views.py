from django.shortcuts import render, get_object_or_404, redirect
from .models import Result
from campaigns.models import ProspectCampaignRelation
from .forms import ResultAddForm
from django.views.generic import FormView, CreateView, ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.http import Http404


class LeadsListView(LoginRequiredMixin, ListView):

    model = Result
    template_name = "results/leads_list.html"

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['campaigns'] = self.request.user.executive.campaign_set.all()
        return context

    def get_queryset(self):
        return super().get_queryset().filter(by=self.request.user.executive)


class ViewsListView(LoginRequiredMixin, ListView):

    model = Result
    template_name = "results/views_list.html"

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['campaigns'] = self.request.user.executive.campaign_set.all()
        return context

    def get_queryset(self):
        return super().get_queryset().filter(by=self.request.user.executive)


class DNCsListView(LoginRequiredMixin, ListView):

    model = Result
    template_name = "results/dncs_list.html"

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['campaigns'] = self.request.user.executive.campaign_set.all()
        return context

    def get_queryset(self):
        return super().get_queryset().filter(by=self.request.user.executive)


def result_add(request, campaign_slug, prospect_id):
    if request.method == 'POST':
        post_dict = request.POST
        pcr = get_object_or_404(ProspectCampaignRelation, campaign__slug=campaign_slug, prospect__id=prospect_id,
                                campaign__executives__in=(request.user.executive, ))
        Result.objects.create(prospect_campaign_relation=pcr,
                                     result_choice=post_dict.get('result_choice'),
                                     by=request.user.executive,
                                     details=post_dict.get('result_details'))
        return redirect('campaigns:prospect_get', slug=pcr.campaign.slug)
    return redirect('campaigns:prospect_get', slug=campaign_slug)

