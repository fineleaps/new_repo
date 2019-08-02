from .models import Prospect
from django.contrib import admin
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from campaigns.models import Campaign, ProspectCampaignRelation


class ProspectAdmin(admin.ModelAdmin):

    list_filter = ('job_title', 'emp_size', 'industry_type', 'state', "prospectcampaignrelation__campaign")
    list_display = ('full_name', 'job_title', 'industry_type', 'state')

    actions = ('assign_campaign', )

    list_per_page = 200

    def assign_campaign(self, request, queryset):

        if 'assign' in request.POST:
            queryset = queryset.exclude(prospectcampaignrelation__campaign=request.POST.get("campaign_id"))
            campaign = get_object_or_404(Campaign, id=request.POST['campaign_id'])
            ProspectCampaignRelation.objects.bulk_create((ProspectCampaignRelation(prospect=prospect, campaign=campaign)
                                                          for prospect in queryset))
            prospect_variable = 'prospects' if queryset.count() > 1 else 'prospect'
            self.message_user(request,
                              "Successfully {prospect_count} {prospect_variable} assigned to campaign {campaign_name}.".format(
                                  prospect_count=queryset.count(),
                                  prospect_variable=prospect_variable,
                                  campaign_name=campaign.name))
            return HttpResponseRedirect(request.get_full_path())
        return render(request, 'campaigns/assign_campaign.html', context={'prospects': queryset, 'campaigns': Campaign.objects.all()})


admin.site.register(Prospect, ProspectAdmin)
