from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DeleteView, UpdateView, FormView, DetailView
from .models import Campaign, ProspectCampaignRelation
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import Http404
from results.forms import ResultAddForm
from prospects.forms import ProspectUpdateAddForm
from prospects.models import Prospect, ProspectUpdate
from django.contrib import messages
from . import alert_messages


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
    prospect_update_add_form = ProspectUpdateAddForm()
    print(555555)
    print(prospect_update_add_form)
    context = {'prospect': prospect, 'campaign': campaign, "prospect_update_add_form": prospect_update_add_form}
    return render(request, 'campaigns/prospect_get.html', context)


def prospect_get_with_prospect(request, slug, prospect_id):
    campaign = get_object_or_404(Campaign, slug=slug, executives__in=(request.user, ))
    prospect = get_object_or_404(Prospect, id=prospect_id, prospectcampaignrelation__campaign=campaign)
    prospect_update_add_form = ProspectUpdateAddForm()

    context = {'prospect': prospect, 'campaign': campaign, "prospect_update_add_form": prospect_update_add_form}
    return render(request, 'campaigns/prospect_get.html', context)


def prospect_update_add(request, campaign_slug, prospect_id):
    form = ProspectUpdateAddForm(request.POST or None)
    if request.POST and form.is_valid():
        form.save(commit=False)
        form.instance.prospect_campaign_relation = get_object_or_404(ProspectCampaignRelation, campaign__slug=campaign_slug, prospect__id=prospect_id)
        form.instance.by = request.user
        form.instance.save()
        messages.success(request, alert_messages.PROSPECT_UPDATE_ADDED_MESSAGE)
    else:
        messages.success(request, alert_messages.PROSPECT_UPDATE_FORM_INVLAID_MESSAGE)
    return redirect("campaigns:prospect_get", slug=campaign_slug, prospect_id=prospect_id)
