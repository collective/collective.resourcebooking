# -*- coding: utf-8 -*-
from collective.resourcebooking.content.ressource_booking import (
    IRessourceBooking,  # NOQA E501
)
from collective.resourcebooking.testing import (  # noqa
    COLLECTIVE_RESOURCEBOOKING_INTEGRATION_TESTING,
)
from plone import api
from plone.api.exc import InvalidParameterError
from plone.app.testing import setRoles
from plone.app.testing import TEST_USER_ID
from plone.dexterity.interfaces import IDexterityFTI
from zope.component import createObject
from zope.component import queryUtility

import unittest


class RessourceBookingIntegrationTest(unittest.TestCase):

    layer = COLLECTIVE_RESOURCEBOOKING_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer["portal"]
        setRoles(self.portal, TEST_USER_ID, ["Manager"])
        self.parent = self.portal

    def test_ct_ressource_booking_schema(self):
        fti = queryUtility(IDexterityFTI, name="RessourceBooking")
        schema = fti.lookupSchema()
        self.assertEqual(IRessourceBooking, schema)

    def test_ct_ressource_booking_fti(self):
        fti = queryUtility(IDexterityFTI, name="RessourceBooking")
        self.assertTrue(fti)

    def test_ct_ressource_booking_factory(self):
        fti = queryUtility(IDexterityFTI, name="RessourceBooking")
        factory = fti.factory
        obj = createObject(factory)

        self.assertTrue(
            IRessourceBooking.providedBy(obj),
            "IRessourceBooking not provided by {0}!".format(
                obj,
            ),
        )

    def test_ct_ressource_booking_adding(self):
        setRoles(self.portal, TEST_USER_ID, ["Contributor"])
        obj = api.content.create(
            container=self.portal,
            type="RessourceBooking",
            id="ressource_booking",
        )

        self.assertTrue(
            IRessourceBooking.providedBy(obj),
            "IRessourceBooking not provided by {0}!".format(
                obj.id,
            ),
        )

        parent = obj.__parent__
        self.assertIn("ressource_booking", parent.objectIds())

        # check that deleting the object works too
        api.content.delete(obj=obj)
        self.assertNotIn("ressource_booking", parent.objectIds())

    def test_ct_ressource_booking_globally_addable(self):
        setRoles(self.portal, TEST_USER_ID, ["Contributor"])
        fti = queryUtility(IDexterityFTI, name="RessourceBooking")
        self.assertTrue(fti.global_allow, "{0} is not globally addable!".format(fti.id))

    def test_ct_ressource_booking_filter_content_type_true(self):
        setRoles(self.portal, TEST_USER_ID, ["Contributor"])
        fti = queryUtility(IDexterityFTI, name="RessourceBooking")
        portal_types = self.portal.portal_types
        parent_id = portal_types.constructContent(
            fti.id,
            self.portal,
            "ressource_booking_id",
            title="RessourceBooking container",
        )
        self.parent = self.portal[parent_id]
        with self.assertRaises(InvalidParameterError):
            api.content.create(
                container=self.parent,
                type="Document",
                title="My Content",
            )
