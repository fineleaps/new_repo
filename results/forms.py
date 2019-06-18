from django import forms
from .models import Result


class ResultAddForm(forms.Form):

    result_choice = forms.ChoiceField(choices=Result.ResultChoices, widget=forms.CheckboxInput)
    details = forms.TextInput()

    class Meta:
        fields = ('result_choice', "details")
