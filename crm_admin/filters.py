from prospects.models import Prospect
from results.models import Result
import django_filters


class ProspectFilter(django_filters.FilterSet):

    JOB_TITLE_CHOICES = [(jt, jt) for jt in Prospect.objects.values_list("job_title", flat=True).distinct()]
    INDUSTRY_TYPE_CHOICES = [(jt, jt) for jt in Prospect.objects.values_list("industry_type", flat=True).distinct()]
    EMP_SIZE_CHOICES = [(jt, jt) for jt in Prospect.objects.values_list("emp_size", flat=True).distinct()]
    STATE_CHOICES = [(jt, jt) for jt in Prospect.objects.values_list("state", flat=True).distinct()]

    job_title = django_filters.ChoiceFilter(choices=JOB_TITLE_CHOICES)
    industry_type = django_filters.ChoiceFilter(choices=INDUSTRY_TYPE_CHOICES)
    emp_size = django_filters.ChoiceFilter(choices=EMP_SIZE_CHOICES)
    state = django_filters.ChoiceFilter(choices=STATE_CHOICES)

    class Meta:
        model = Prospect
        fields = ("job_title", "industry_type", "emp_size", "state")


class ResultFilter(django_filters.FilterSet):
    date = django_filters.DateFilter(field_name="on__date", label="by date")
    date_period = django_filters.DateRangeFilter(field_name="on", label="By Date Period")
    date_duration = django_filters.DateFromToRangeFilter(field_name="on", lookup_expr="date__in", label="By Date Duration")

    class Meta:
        model = Result
        fields = ['by', 'prospect_campaign_relation__campaign', 'result_choice', 'date_period', "date_duration", "date"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.filters['by'].label = "By Executive"
        self.filters['prospect_campaign_relation__campaign'].label = "By Campaign"
        self.filters['result_choice'].label = "By Result"
        self.filters['by'].extra.update(
            {'empty_label': 'All Executives'})
        self.filters['prospect_campaign_relation__campaign'].extra.update(
            {'empty_label': 'All Campaigns'})
        self.filters['result_choice'].extra.update(
            {'empty_label': 'All Results'})
