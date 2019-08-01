from .models import Result
import django_filters
from django import forms
from django_filters import widgets


class ResultFilter(django_filters.FilterSet):
    date = django_filters.DateFilter(field_name="on__date", label="by date")
    date_period = django_filters.DateRangeFilter(field_name="on", label="By Date Period")
    date_duration = django_filters.DateFromToRangeFilter(field_name="on", lookup_expr="date__in",
                                                         label="By Date Duration")

    class Meta:
        model = Result
        fields = ['prospect_campaign_relation__campaign', 'result_choice', 'date_period', "date_duration", "date"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.filters['prospect_campaign_relation__campaign'].label = "By Campaign"
        self.filters['result_choice'].label = "By Result"
        self.filters['prospect_campaign_relation__campaign'].extra.update(
            {'empty_label': 'All Campaigns'})
        self.filters['result_choice'].extra.update(
            {'empty_label': 'All Results'})
