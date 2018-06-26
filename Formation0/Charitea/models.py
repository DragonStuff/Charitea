from django.urls import reverse
from django_extensions.db.fields import AutoSlugField
from django.db.models import *
from django.conf import settings
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth import get_user_model
from django.contrib.auth import models as auth_models
from django.db import models as models
from django_extensions.db import fields as extension_fields


class participant(models.Model):

    # Fields
    name = models.CharField(max_length=255)
    slug = extension_fields.AutoSlugField(populate_from='name', blank=True)
    created = models.DateTimeField(auto_now_add=True, editable=False)
    last_updated = models.DateTimeField(auto_now=True, editable=False)
    points = models.PositiveIntegerField()
    custom_bio = models.CharField(max_length=30)

    class Meta:
        ordering = ('-created',)

    def __str__(self):
        return u'%s' % self.name

    def __unicode__(self):
        return u'%s' % self.slug

    def get_absolute_url(self):
        return reverse('Charitea_participant_detail', args=(self.slug,))


    def get_update_url(self):
        return reverse('Charitea_participant_update', args=(self.slug,))


class donation(models.Model):

    # Relationship Fields
    donor = models.ForeignKey(participant, on_delete=models.CASCADE)

    # Fields
    slug = extension_fields.AutoSlugField(populate_from='donor', blank=True)
    created = models.DateTimeField(auto_now_add=True, editable=False)
    last_updated = models.DateTimeField(auto_now=True, editable=False)
    amount = models.PositiveSmallIntegerField()

    class Meta:
        ordering = ('-created',)
    
    def __str__(self):
        return u'%s donated $%s' % (self.donor.name, self.amount)

    def __unicode__(self):
        return u'%s' % self.slug

    def get_absolute_url(self):
        return reverse('Charitea_donation_detail', args=(self.slug,))


    def get_update_url(self):
        return reverse('Charitea_donation_update', args=(self.slug,))


