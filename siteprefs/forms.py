from django import forms
from django.forms import Textarea

from siteprefs.models import Preference


class SpecialForm(forms.ModelForm):
    class Meta:
        model = Preference
        fields = '__all__'
        widgets = {
            'value': Textarea(attrs={'rows': 20, 'class' : 'editor'}),
        }