from django.contrib import admin
from django import forms
from .models import participant, donation

class participantAdminForm(forms.ModelForm):

    class Meta:
        model = participant
        fields = '__all__'


class participantAdmin(admin.ModelAdmin):
    form = participantAdminForm
    list_display = ['name', 'slug', 'created', 'last_updated', 'points', 'custom_bio']
    readonly_fields = ['name', 'slug', 'created', 'last_updated', 'points', 'custom_bio']

admin.site.register(participant, participantAdmin)


class donationAdminForm(forms.ModelForm):

    class Meta:
        model = donation
        fields = '__all__'


class donationAdmin(admin.ModelAdmin):
    form = donationAdminForm
    list_display = ['slug', 'created', 'last_updated', 'amount']
    readonly_fields = ['slug', 'created', 'last_updated', 'amount']

admin.site.register(donation, donationAdmin)


