# -*- coding: utf-8 -*-
from collective.resourcebooking.testing import (
    COLLECTIVE_RESOURCEBOOKING_FUNCTIONAL_TESTING,
)
from collective.resourcebooking.testing import (
    COLLECTIVE_RESOURCEBOOKING_INTEGRATION_TESTING,
)
from plone.app.testing import setRoles
from plone.app.testing import TEST_USER_ID

import unittest


class SubscriberIntegrationTest(unittest.TestCase):

    layer = COLLECTIVE_RESOURCEBOOKING_INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer["portal"]
        setRoles(self.portal, TEST_USER_ID, ["Manager"])


class SubscriberFunctionalTest(unittest.TestCase):

    layer = COLLECTIVE_RESOURCEBOOKING_FUNCTIONAL_TESTING

    def setUp(self):
        self.portal = self.layer["portal"]
        setRoles(self.portal, TEST_USER_ID, ["Manager"])
