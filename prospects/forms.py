from django import forms
from .models import ProspectUpdate


class ProspectUpdateAddForm(forms.ModelForm):

    class Meta:
        model = ProspectUpdate
        exclude = ('prospect_campaign_relation', "by", "is_approved", "created_on")

    # def __init__(self, prospect=None, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     if prospect:
    #         self.fields['phone'].initial = prospect.phone
    #         self.fields['direct_or_extension'].initial = prospect.direct_or_extension
    #         self.fields['email'].initial = prospect.email
    #         self.fields['job_title'].initial = prospect.job_title
    #         self.fields['industry_type'].initial = prospect.industry_type
    #         self.fields['company'].initial = prospect.company
    #         self.fields['emp_size'].initial = prospect.emp_size
    #         self.fields['website'].initial = prospect.website
    #
