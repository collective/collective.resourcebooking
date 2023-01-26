# -*- coding: utf-8 -*-
# from plone.app.textfield import RichText
# from plone.supermodel.directives import fieldset
# from plone.namedfile import field as namedfile
# from z3c.form.browser.radio import RadioFieldWidget
from plone.autoform import directives
from collective.resourcebooking import _
from plone.dexterity.content import Item
from plone.supermodel import model
from zope import schema
from zope.interface import implementer


class IBooking(model.Schema):
    """Marker interface and Dexterity Python Schema for Booking"""
    # directives.mode(title="hidden")
    title = schema.TextLine(
        title=_(
            u'Computed Title',
        ),
        required=False,
        readonly=False,
    )

    ressource = schema.Choice(
        title=_(
            u'Ressource',
        ),
        description=_(
            u'Choose a ressource to book',
        ),
        vocabulary="collective.resourcebooking.AvailableRessources",
        default=u"",
        # defaultFactory=get_default_ressource,
        required=True,
        readonly=False,
    )

    start = schema.Datetime(
        title=_(
            "Start",
        ),
        # defaultFactory=get_default_start,
        required=True,
    )

    end = schema.Datetime(
        title=_(
            "End",
        ),
        # defaultFactory=get_default_start,
        required=True,
    )


@implementer(IBooking)
class Booking(Item):
    """Content-type class for IBooking"""

    @property
    def title(self):
        computed_title = ""
        if hasattr(self, "ressource"):
            computed_title = self.ressource
        if hasattr(self, "start") and hasattr(self, "end"):
            computed_title += f": {self.start.isoformat()}-{self.end.isoformat()}"
        return computed_title

    @title.setter
    def title(self, value):
        return None
