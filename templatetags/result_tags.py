from django import template
from results.models import Result
from django.shortcuts import get_list_or_404, get_object_or_404
from campaigns.models import Campaign
from portal.models import User

register = template.Library()


@register.filter
def get_leads_by_campaign(campaign_id, executive_id):
    executive = get_object_or_404(User, id=executive_id)
    return executive.result_set.filter(result_choice="Lead", prospect_campaign_relation__campaign_id=campaign_id)
