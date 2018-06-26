from . import models

from rest_framework import serializers


class participantSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.participant
        fields = (
            'slug', 
            'name', 
            'created', 
            'last_updated', 
            'points', 
            'custom_bio', 
        )


class donationSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.donation
        fields = (
            'slug', 
            'name', 
            'created', 
            'last_updated', 
            'amount', 
        )


