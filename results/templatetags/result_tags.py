from django import template
from results.models import Result
from django.shortcuts import get_list_or_404, get_object_or_404
from campaigns.models import Campaign
from portal.models import Executive

register = template.Library()


@register.simple_tag
def get_leads_by_campaign(campaign_id, executive_id):
    executive = get_object_or_404(Executive, id=executive_id)
    return executive.result_set.filter(result_choice="Lead", prospect_campaign_relation__campaign_id=campaign_id).count()


@register.simple_tag
def get_dncs_by_campaign(campaign_id, executive_id):
    executive = get_object_or_404(Executive, id=executive_id)
    return executive.result_set.filter(result_choice="DNC", prospect_campaign_relation__campaign_id=campaign_id).count()


@register.simple_tag
def get_views_by_campaign(campaign_id, executive_id):
    executive = get_object_or_404(Executive, id=executive_id)
    return executive.result_set.filter(result_choice="View", prospect_campaign_relation__campaign_id=campaign_id).count()
