from django.shortcuts import render, get_object_or_404, redirect
from .models import Result
from campaigns.models import ProspectCampaignRelation
from .forms import ResultAddForm
from django.views.generic import FormView, CreateView, ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.http import Http404


# class ResultAddView(LoginRequiredMixin, CreateView):
#     form_class = ResultAddForm
#     template_name = "campaigns/prospect_get.html"
#     success_url = reverse_lazy("campaigns:prospect_get")
#     model = Result
#
#     def form_valid(self, form):
#         pcr = get_object_or_404(ProspectCampaignRelation, campaign__slug=self.kwargs.get('campaign_slug'),
#                                 prospect__id=self.kwargs.get('prospect_id'),
#                                 campaign__executives__in=(self.request.user.executive,))
#         form.instance.by = self.request.user
#         form.instance.prospect_campaign_relation = pcr
#         form.save()
#         return redirect("campaigns:prospect_get", slug=pcr.campaign.slug)
#
#     def get(self, *args, **kwargs):
#         return redirect("campaigns:prospect_get")
#
#

#
# class ResultAddView(LoginRequiredMixin, FormView):
#
#     form_class = ResultAddForm
#     template_name = "campaigns/prospect_get.html"
#
#     def form_valid(self, form):
#         print("///////////////--------------------------////////////////////////////////")
#
#         post_dict = form.cleaned_data
#         pcr = get_object_or_404(ProspectCampaignRelation, campaign__slug=self.kwargs.get('campaign_slug'),
#                                 prospect__id=self.kwargs.get('prospect_id'), campaign__executives__in=(self.request.user.executive,))
#         re = Result.objects.create(prospect_campaign_relation=pcr,
#                               result_choice=post_dict.get('result_choice'),
#                               by=self.request.user.executive,
#                               details=post_dict.get('details'))
#         print(re)
#         print("///////////////--------------------------////////////////////////////////")
#         return redirect('campaigns:prospect_get', kwargs={'slug': pcr.campaign.slug})
#
#     # def get(self, request, *args, **kwargs):
#     #     return redirect("campaigns:prospect_get", slug=self.kwargs.get('slug'))

#
def result_add(request, campaign_slug, prospect_id):
    if request.method == 'POST':
        form = ResultAddForm(request.POST)
        if form.is_valid():
            post_dict = form.data
            print(post_dict)
            print("---------------------------")
            pcr = get_object_or_404(ProspectCampaignRelation, campaign__slug=campaign_slug, prospect__id=prospect_id,
                                    campaign__executives__in=(request.user.executive, ))
            Result.objects.create(prospect_campaign_relation=pcr,
                                         result_choice=post_dict.get('result_choice'),
                                         by=request.user.executive,
                                         details=post_dict.get('details'))
            return redirect('campaigns:prospect_get', slug=pcr.campaign.slug)
        else:
            raise Http404("Bad Request")

    return redirect('campaigns:prospect_get', slug=campaign_slug)


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
