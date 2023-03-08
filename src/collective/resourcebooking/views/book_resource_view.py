# -*- coding: utf-8 -*-

from datetime import date
from datetime import timedelta
from plone import api
from plone.protect.utils import safeWrite
from Products.Five.browser import BrowserView
from zope.interface import implementer
from zope.interface import Interface


class IBookResourceView(Interface):
    """Marker Interface for IBookResourceView"""


@implementer(IBookResourceView)
class BookResourceView(BrowserView):
    def __call__(self):
        safeWrite(self.context, self.request)
        wday = self.request.get("wday")
        today = date.today()
        day = today + timedelta(days = (int(wday)-today.weekday()))
        booking = api.content.create(
            container=self.context,
            type="Booking",
            title=self.request.get("resource"),
            resource=self.request.get("resource"),
            day=day,
            timeslot=int(self.request.get("timeslot")),
        )
        rb_container = self.context.get_resource_booking_container()
        return self.request.response.redirect(rb_container.absolute_url(), status=301)
