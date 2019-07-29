from prospects.models import Prospect
from results.models import Result
import django_filters


class ProspectFilter(django_filters.FilterSet):

    # JOB_TITLE_CHOICES = [(jt, jt) for jt in Prospect.objects.values_list("job_title", flat=True).distinct()]
    # INDUSTRY_TYPE_CHOICES = [(jt, jt) for jt in Prospect.objects.values_list("industry_type", flat=True).distinct()]
    # EMP_SIZE_CHOICES = [(jt, jt) for jt in Prospect.objects.values_list("emp_size", flat=True).distinct()]
    # STATE_CHOICES = [(jt, jt) for jt in Prospect.objects.values_list("state", flat=True).distinct()]
    #
    # job_title = django_filters.ChoiceFilter(choices=JOB_TITLE_CHOICES)
    # industry_type = django_filters.ChoiceFilter(choices=INDUSTRY_TYPE_CHOICES)
    # emp_size = django_filters.ChoiceFilter(choices=EMP_SIZE_CHOICES)
    # state = django_filters.ChoiceFilter(choices=STATE_CHOICES)

    class Meta:
        model = Prospect
        fields = ("job_title", "industry_type", "emp_size", "state")


class ResultFilter(django_filters.FilterSet):
    on = django_filters.DateFilter(field_name="on__date", label="by date")
    d_range = django_filters.DateRangeFilter(field_name="on", label="By Duration")
    date_range = django_filters.DateFromToRangeFilter(field_name="on", lookup_expr="date__in")

    class Meta:
        model = Result
        fields = ['by', 'on', 'prospect_campaign_relation__campaign', 'result_choice', 'date_range']
