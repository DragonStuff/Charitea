import unittest
from django.urls import reverse
from django.test import Client
from .models import participant, donation
from django.contrib.auth.models import User
from django.contrib.auth.models import Group
from django.contrib.contenttypes.models import ContentType


def create_django_contrib_auth_models_user(**kwargs):
    defaults = {}
    defaults["username"] = "username"
    defaults["email"] = "username@tempurl.com"
    defaults.update(**kwargs)
    return User.objects.create(**defaults)


def create_django_contrib_auth_models_group(**kwargs):
    defaults = {}
    defaults["name"] = "group"
    defaults.update(**kwargs)
    return Group.objects.create(**defaults)


def create_django_contrib_contenttypes_models_contenttype(**kwargs):
    defaults = {}
    defaults.update(**kwargs)
    return ContentType.objects.create(**defaults)


def create_participant(**kwargs):
    defaults = {}
    defaults["name"] = "name"
    defaults["points"] = "points"
    defaults["custom_bio"] = "custom_bio"
    defaults.update(**kwargs)
    return participant.objects.create(**defaults)


def create_donation(**kwargs):
    defaults = {}
    defaults["name"] = "name"
    defaults["amount"] = "amount"
    defaults.update(**kwargs)
    if "donor" not in defaults:
        defaults["donor"] = create_participant()
    return donation.objects.create(**defaults)


class participantViewTest(unittest.TestCase):
    '''
    Tests for participant
    '''
    def setUp(self):
        self.client = Client()

    def test_list_participant(self):
        url = reverse('Charitea_participant_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_create_participant(self):
        url = reverse('Charitea_participant_create')
        data = {
            "name": "name",
            "points": "points",
            "custom_bio": "custom_bio",
        }
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, 302)

    def test_detail_participant(self):
        participant = create_participant()
        url = reverse('Charitea_participant_detail', args=[participant.slug,])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_update_participant(self):
        participant = create_participant()
        data = {
            "name": "name",
            "points": "points",
            "custom_bio": "custom_bio",
        }
        url = reverse('Charitea_participant_update', args=[participant.slug,])
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)


class donationViewTest(unittest.TestCase):
    '''
    Tests for donation
    '''
    def setUp(self):
        self.client = Client()

    def test_list_donation(self):
        url = reverse('Charitea_donation_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_create_donation(self):
        url = reverse('Charitea_donation_create')
        data = {
            "name": "name",
            "amount": "amount",
            "donor": create_participant().pk,
        }
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, 302)

    def test_detail_donation(self):
        donation = create_donation()
        url = reverse('Charitea_donation_detail', args=[donation.slug,])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_update_donation(self):
        donation = create_donation()
        data = {
            "name": "name",
            "amount": "amount",
            "donor": create_participant().pk,
        }
        url = reverse('Charitea_donation_update', args=[donation.slug,])
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)


