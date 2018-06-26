from . import models
from . import serializers
from rest_framework import viewsets, permissions


class participantViewSet(viewsets.ModelViewSet):
    """ViewSet for the participant class"""

    queryset = models.participant.objects.all()
    serializer_class = serializers.participantSerializer
    permission_classes = [permissions.IsAuthenticated]


class donationViewSet(viewsets.ModelViewSet):
    """ViewSet for the donation class"""

    queryset = models.donation.objects.all()
    serializer_class = serializers.donationSerializer
    permission_classes = [permissions.IsAuthenticated]


