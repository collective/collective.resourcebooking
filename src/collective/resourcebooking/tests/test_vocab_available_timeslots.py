# -*- coding: utf-8 -*-
from collective.resourcebooking import _
from collective.resourcebooking.testing import (  # noqa
    COLLECTIVE_RESOURCEBOOKING_INTEGRATION_TESTING,
)
from plone.app.testing import setRoles
from plone.app.testing import TEST_USER_ID
from zope.component import getUtility
from zope.schema.interfaces import IVocabularyFactory
from zope.schema.interfaces import IVocabularyTokenized

import unittest


class AvailableTimeslotsIntegrationTest(unittest.TestCase):

    layer = COLLECTIVE_RESOURCEBOOKING_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer["portal"]
        setRoles(self.portal, TEST_USER_ID, ["Manager"])

    def test_vocab_available_timeslots(self):
        vocab_name = "collective.resourcebooking.AvailableTimeslots"
        factory = getUtility(IVocabularyFactory, vocab_name)
        self.assertTrue(IVocabularyFactory.providedBy(factory))

        vocabulary = factory(self.portal)
        self.assertTrue(IVocabularyTokenized.providedBy(vocabulary))
        self.assertEqual(
            vocabulary.getTerm("sony-a7r-iii").title,
            _("Sony Aplha 7R III"),
        )
