from .models import ProspectUpdate
import django_filters
from django import forms
from django_filters import widgets


class ProspectUpdateFilter(django_filters.FilterSet):

    class Meta:
        model = ProspectUpdate
        fields = ['prospect_campaign_relation__campaign', 'by', 'created_on', "is_approved"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.filters['prospect_campaign_relation__campaign'].label = "By Campaign"
        self.filters['prospect_campaign_relation__campaign'].extra.update(
            {'empty_label': 'All Campaigns'})