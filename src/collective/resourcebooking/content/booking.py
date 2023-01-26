# -*- coding: utf-8 -*-
# from plone.app.textfield import RichText
# from plone.autoform import directives
# from plone.supermodel.directives import fieldset
# from plone.namedfile import field as namedfile
# from z3c.form.browser.radio import RadioFieldWidget
from collective.resourcebooking import _
from plone.dexterity.content import Item
from plone.supermodel import model
from zope import schema
from zope.interface import implementer


class IBooking(model.Schema):
    """Marker interface and Dexterity Python Schema for Booking"""

    start = schema.Datetime(
        title=_(
            u'Start',
        ),
        # defaultFactory=get_default_start,
        required=True,
    )

    end = schema.Datetime(
        title=_(
            u'End',
        ),
        # defaultFactory=get_default_start,
        required=True,
    )


@implementer(IBooking)
class Booking(Item):
    """Content-type class for IBooking"""
