# -*- coding: utf-8 -*-
from collective.resourcebooking.content.ressources import IRessources  # NOQA E501
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


class RessourcesIntegrationTest(unittest.TestCase):

    layer = COLLECTIVE_RESOURCEBOOKING_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer["portal"]
        setRoles(self.portal, TEST_USER_ID, ["Manager"])
        portal_types = self.portal.portal_types
        parent_id = portal_types.constructContent(
            "RessourceBooking",
            self.portal,
            "parent_container",
            title="Parent container",
        )
        self.parent = self.portal[parent_id]

    def test_ct_ressources_schema(self):
        fti = queryUtility(IDexterityFTI, name="Ressources")
        schema = fti.lookupSchema()
        self.assertEqual(IRessources, schema)

    def test_ct_ressources_fti(self):
        fti = queryUtility(IDexterityFTI, name="Ressources")
        self.assertTrue(fti)

    def test_ct_ressources_factory(self):
        fti = queryUtility(IDexterityFTI, name="Ressources")
        factory = fti.factory
        obj = createObject(factory)

        self.assertTrue(
            IRessources.providedBy(obj),
            "IRessources not provided by {0}!".format(
                obj,
            ),
        )

    def test_ct_ressources_adding(self):
        setRoles(self.portal, TEST_USER_ID, ["Contributor"])
        obj = api.content.create(
            container=self.parent,
            type="Ressources",
            id="ressources",
        )

        self.assertTrue(
            IRessources.providedBy(obj),
            "IRessources not provided by {0}!".format(
                obj.id,
            ),
        )

        parent = obj.__parent__
        self.assertIn("ressources", parent.objectIds())

        # check that deleting the object works too
        api.content.delete(obj=obj)
        self.assertNotIn("ressources", parent.objectIds())

    def test_ct_ressources_globally_not_addable(self):
        setRoles(self.portal, TEST_USER_ID, ["Contributor"])
        fti = queryUtility(IDexterityFTI, name="Ressources")
        self.assertFalse(fti.global_allow, "{0} is globally addable!".format(fti.id))

    def test_ct_ressources_filter_content_type_true(self):
        setRoles(self.portal, TEST_USER_ID, ["Contributor"])
        fti = queryUtility(IDexterityFTI, name="Ressources")
        portal_types = self.portal.portal_types
        parent_id = portal_types.constructContent(
            fti.id,
            self.portal,
            "ressources_id",
            title="Ressources container",
        )
        self.parent = self.portal[parent_id]
        with self.assertRaises(InvalidParameterError):
            api.content.create(
                container=self.parent,
                type="Document",
                title="My Content",
            )
