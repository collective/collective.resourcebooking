# -*- coding: utf-8 -*-
from collective.resourcebooking import _
from collective.resourcebooking.testing import (  # noqa
    COLLECTIVE_RESOURCEBOOKING_INTEGRATION_TESTING,
)
from plone import api
from plone.app.testing import setRoles
from plone.app.testing import TEST_USER_ID
from zope.component import getUtility
from zope.schema.interfaces import IVocabularyFactory
from zope.schema.interfaces import IVocabularyTokenized

import unittest


class AvailableRessourcesIntegrationTest(unittest.TestCase):

    layer = COLLECTIVE_RESOURCEBOOKING_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer["portal"]
        setRoles(self.portal, TEST_USER_ID, ["Manager"])
        roombookings = api.content.create(
            container=self.portal, type="RessourceBooking", title="roombookings"
        )
        self.bookings = api.content.create(
            container=roombookings, type="Bookings", title="Bookings"
        )
        self.ressources = api.content.create(
            container=roombookings, type="Ressources", title="Rooms"
        )
        self.room1 = api.content.create(
            container=self.ressources, type="Ressource", title="Room 1"
        )
        self.room2 = api.content.create(
            container=self.ressources, type="Ressource", title="Room 2"
        )

    def test_vocab_available_ressources(self):
        booking = api.content.create(
            container=self.bookings, type="Booking", title="Test Booking 1"
        )
        vocab_name = "collective.resourcebooking.AvailableRessources"
        factory = getUtility(IVocabularyFactory, vocab_name)
        self.assertTrue(IVocabularyFactory.providedBy(factory))

        vocabulary = factory(self.portal)
        self.assertTrue(IVocabularyTokenized.providedBy(vocabulary))
        self.assertEqual(
            vocabulary.getTerm("room-2").title,
            "Room 2",
        )

    def test_vocab_available_ressources_on_booking(self):
        booking = api.content.create(
            container=self.bookings,
            type="Booking",
            title="Test Booking",
            id="test-booking",
        )
        vocab_name = "collective.resourcebooking.AvailableRessources"
        factory = getUtility(IVocabularyFactory, vocab_name)
        self.assertTrue(IVocabularyFactory.providedBy(factory))
        vocabulary = factory(booking)
        self.assertTrue(IVocabularyTokenized.providedBy(vocabulary))
        self.assertEqual(
            vocabulary.getTerm("room-1").title,
            "Room 1",
        )
