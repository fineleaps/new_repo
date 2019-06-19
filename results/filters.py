from .models import Result
import django_filters
from django import forms
from django_filters import widgets


class ResultFilter(django_filters.FilterSet):

    # by = django_filters.Cho.
    # date_range = django_filters.DateFromToRangeFilter(field_name="on", lookup_expr="date__in",
    #                                                   widget=widgets.DateRangeWidget(attrs={"id": "jqueryDateRangePicker "}))
    #
    on = django_filters.DateFilter(widget=forms.DateInput(attrs={"id": "jqueryDatePicker"}))

    d_range = django_filters.DateRangeFilter(field_name="on", label="date")

    date_range = django_filters.DateFromToRangeFilter(field_name="on", lookup_expr="date__in",
                                                      widget=widgets.DateRangeWidget())

    class Meta:
        model = Result
        fields = ['on', 'prospect_campaign_relation__campaign', 'result_choice', 'date_range']
