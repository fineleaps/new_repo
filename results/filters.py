from .models import Result
import django_filters
from django import forms
from django_filters import widgets


class ResultFilter(django_filters.FilterSet):
    on = django_filters.DateFilter(field_name="on__date", label="by date")
    d_range = django_filters.DateRangeFilter(field_name="on", label="By Duration")
    date_range = django_filters.DateFromToRangeFilter(field_name="on", lookup_expr="date__in")
    # prospect_campaign_relation__campaign = django_filters.ModelChoiceFilter(label="")

    class Meta:
        model = Result
        fields = ['on', 'prospect_campaign_relation__campaign', 'result_choice', 'date_range']
