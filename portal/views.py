from django.views.generic import View, DetailView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Executive
from django.urls import reverse_lazy
from .forms import ProfileUpdateForm
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash, get_user_model
from django.contrib.auth.forms import PasswordChangeForm
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from . import alert_messages
from results.models import Result
from django.db.models import Count, Avg, Min, Max, Sum, Q
from campaigns.models import Campaign


@login_required
def password_change(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            messages.success(request, alert_messages.PASSWORD_CHANGED_MESSAGE)
            return redirect('portal:home')
        else:
            messages.error(request, alert_messages.FORM_INVALID_MESSAGE)
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'portal/password_change.html', {
        'form': form
    })


@login_required
def home(request):
    campaigns = Campaign.objects.annotate(results=Sum("prospectcampaignrelation__result"),
                                          leads=Sum("prospectcampaignrelation__result",
                                                    filter=Q(prospectcampaignrelation__result__result_choice="Lead")),
                                          views=Sum("prospectcampaignrelation__result",
                                                    filter=Q(prospectcampaignrelation__result__result_choice="View")),
                                          dncs=Sum("prospectcampaignrelation__result",
                                                    filter=Q(prospectcampaignrelation__result__result_choice="DNC")),
                                          )
    return render(request, "portal/home.html", {"campaigns": campaigns})


class HomeView(LoginRequiredMixin, View):

    # def get(self, request):
    #     if request.user.is_superuser:
    #         return redirect('crm_admin:home')
    #     else:
    #         return render(request, 'portal/home.html')
    def get(self, request):
        return render(request, 'portal/home.html')

    # def get_context_data(self):
    #     context = super().get_context_data()
    #     months = "nmdsalkfm"
    #     context["months"] = months
    #     return context


class ProfileView(LoginRequiredMixin, DetailView):

    template_name = "portal/profile.html"
    context_object_name = "executive"

    def get_object(self, queryset=None):
        return self.request.user.executive


class ProfileUpdateView(LoginRequiredMixin, UpdateView):

    model = Executive
    form_class = ProfileUpdateForm
    template_name = "portal/profile_update.html"
    success_url = reverse_lazy("portal:profile_update")

    def get_object(self, queryset=None):
        return self.request.user.executive

    def form_valid(self, form):
        messages.success(self.request, alert_messages.PROFILE_UPDATED_MESSAGE)
        return super().form_valid(form)



# e
# @login_required
# def profile(request):
#
#     context = {"executive": }
#
#     return render(rquest, 'portal/profile.html', context)
#
