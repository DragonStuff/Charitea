from django.views.generic import DetailView, ListView, UpdateView, CreateView
from .models import participant, donation
from .forms import participantForm, donationForm
from django.shortcuts import HttpResponse, render

def indexview(request):
    latest_donations = donation.objects.all().order_by('-last_updated').values()[:5]
    context = {'latest_donations': latest_donations}
    return render(request, 'Charitea/index.html', context)

class participantListView(ListView):
    model = participant


class participantCreateView(CreateView):
    model = participant
    form_class = participantForm


class participantDetailView(DetailView):
    model = participant


class participantUpdateView(UpdateView):
    model = participant
    form_class = participantForm


class donationListView(ListView):
    model = donation


class donationCreateView(CreateView):
    model = donation
    form_class = donationForm


class donationDetailView(DetailView):
    model = donation


class donationUpdateView(UpdateView):
    model = donation
    form_class = donationForm

