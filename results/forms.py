from django import forms
from .models import Result


class ResultAddForm(forms.Form):

    # ResultChoicesList = ("Lead", "View", "DNC")
    #
    # result_choice = forms.ChoiceField(choices=ResultChoicesList, widget=forms.CheckboxInput)
    # details = forms.TextInput()

    class Meta:
        fields = ('result_choice', "details")
