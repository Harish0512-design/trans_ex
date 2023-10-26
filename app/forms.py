from django import forms


class FilterForm(forms.Form):
    from_date = forms.DateField()
    to_date = forms.DateField()
