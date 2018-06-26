from django import forms
from .models import participant, donation


class participantForm(forms.ModelForm):
    class Meta:
        model = participant
        fields = ['name', 'points', 'custom_bio']


class donationForm(forms.ModelForm):
    class Meta:
        model = donation
        fields = ['amount', 'donor']


