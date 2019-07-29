from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DeleteView, UpdateView, FormView, DetailView
from .models import Campaign, ProspectCampaignRelation
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import Http404
from results.forms import ResultAddForm


class CampaignListView(LoginRequiredMixin, ListView):

    model = Campaign
    template_name = "campaigns/list.html"
    context_object_name = "campaigns"

    def get_queryset(self):
        return super().get_queryset().filter(executives__in=(self.request.user, ), is_active=True)


class CampaignDetailView(LoginRequiredMixin, DetailView):

    model = Campaign
    template_name = "campaigns/detail.html"
    context_object_name = "campaign"

    def get_object(self, queryset=None):
        campaign = super().get_object()
        if self.request.user in campaign.executives.all():
            return campaign
        else:
            raise Http404("No Campaign Found")


def prospect_get(request, slug):
    campaign = get_object_or_404(Campaign, slug=slug, executives__in=(request.user, ))
    prospect = campaign.prospect_get
    context = {'prospect': prospect, 'campaign': campaign}
    return render(request, 'campaigns/prospect_get.html', context)

