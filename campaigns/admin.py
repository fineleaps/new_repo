from django.contrib import admin
from .models import Campaign, ProspectCampaignRelation

admin.site.register(Campaign)
admin.site.register(ProspectCampaignRelation)
