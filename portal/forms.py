from django import forms
from .models import Executive


class ProfileUpdateForm(forms.ModelForm):

    first_name = forms.CharField(disabled=True, required=False)
    last_name = forms.CharField(disabled=True, required=False)
    date_of_birth = forms.DateField(disabled=True, required=False)
    employee_id = forms.CharField(disabled=True, required=False)

    class Meta:

        model = Executive
        fields = ('first_name', 'last_name', 'email', 'phone', 'date_of_birth', 'employee_id')


