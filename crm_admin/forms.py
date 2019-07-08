from django import forms
from campaigns.models import Campaign


class CampaignUpdateForm(forms.ModelForm):

    class Meta:

        model = Campaign
        fields = ('name', 'aim', 'is_active', 'script', 'details', 'start_date', 'end_date', 'executives')


class CampaignAddForm(forms.ModelForm):

    class Meta:
        model = Campaign
        fields = ('name', 'aim', 'is_active', 'script', 'details', 'start_date', 'end_date', 'executives')
