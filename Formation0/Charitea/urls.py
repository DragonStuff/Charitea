from django.urls import path, include
from rest_framework import routers

from . import api
from . import views

router = routers.DefaultRouter()
router.register(r'participant', api.participantViewSet)
router.register(r'donation', api.donationViewSet)


urlpatterns = (
    # urls for Django Rest Framework API
    path('api/v1/', include(router.urls)),

    # Main page
    path('', views.indexview),
)

urlpatterns += (
    # urls for participant
    path('participant/', views.participantListView.as_view(), name='Charitea_participant_list'),
    path('participant/create/', views.participantCreateView.as_view(), name='Charitea_participant_create'),
    path('participant/detail/<slug:slug>/', views.participantDetailView.as_view(), name='Charitea_participant_detail'),
    path('participant/update/<slug:slug>/', views.participantUpdateView.as_view(), name='Charitea_participant_update'),
)

urlpatterns += (
    # urls for donation
    path('donation/', views.donationListView.as_view(), name='Charitea_donation_list'),
    path('donation/create/', views.donationCreateView.as_view(), name='Charitea_donation_create'),
    path('donation/detail/<slug:slug>/', views.donationDetailView.as_view(), name='Charitea_donation_detail'),
    path('donation/update/<slug:slug>/', views.donationUpdateView.as_view(), name='Charitea_donation_update'),
)

