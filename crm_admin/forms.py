from django import forms
from campaigns.models import Campaign
from clients.models import Client


class CampaignUpdateForm(forms.ModelForm):

    class Meta:

        model = Campaign
        fields = ('client', 'name', 'aim', 'is_active', 'script', 'details', 'start_date', 'end_date', 'executives')


class CampaignAddForm(forms.ModelForm):

    class Meta:
        model = Campaign
        fields = ('client', 'name', 'aim', 'is_active', 'script', 'details', 'start_date', 'end_date', 'executives')


class ClientUpdateForm(forms.ModelForm):

    class Meta:

        model = Client
        exclude = ('added_on', 'slug', )


class ClientAddForm(forms.ModelForm):

    class Meta:
        model = Client
        exclude = ('added_on', 'slug', )
