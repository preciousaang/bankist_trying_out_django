from django import forms


class JournalForm(forms.Form):
    title = forms.CharField(max_length=20, min_length=5)
