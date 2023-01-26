# -*- coding: utf-8 -*-

from plone import api
from collective.resourcebooking import _
from plone.dexterity.interfaces import IDexterityContent
from zope.globalrequest import getRequest
from zope.interface import implementer
from zope.schema.interfaces import IVocabularyFactory
from zope.schema.vocabulary import SimpleTerm
from zope.schema.vocabulary import SimpleVocabulary
from Products.CMFCore.interfaces import ISiteRoot
from collective.resourcebooking.content.ressource_booking import IRessourceBooking


class VocabItem(object):
    def __init__(self, token, value):
        self.token = token
        self.value = value


@implementer(IVocabularyFactory)
class AvailableRessources(object):
    """ """

    def __call__(self, context):
        def get_resource_booking_container(obj):
            if ISiteRoot.providedBy(obj):
                return obj
            parent = obj.__parent__
            if not IRessourceBooking.providedBy(parent):
                return get_resource_booking_container(parent)
            return parent
        resource_booking = get_resource_booking_container(context)

        items = [VocabItem(item.id, item.Title) for item in api.content.find(context=resource_booking, portal_type="Ressource", sort_on="sortable_title") if item]
        # Fix context if you are using the vocabulary in DataGridField.
        # See https://github.com/collective/collective.z3cform.datagridfield/issues/31:  # NOQA: 501
        if not IDexterityContent.providedBy(context):
            req = getRequest()
            context = req.PARENTS[0]

        # create a list of SimpleTerm items:
        terms = []
        for item in items:
            terms.append(
                SimpleTerm(
                    value=item.token,
                    token=str(item.token),
                    title=item.value,
                )
            )
        # Create a SimpleVocabulary from the terms list and return it:
        return SimpleVocabulary(terms)


AvailableRessourcesFactory = AvailableRessources()
