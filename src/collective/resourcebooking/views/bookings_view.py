# -*- coding: utf-8 -*-

# from collective.resourcebooking import _
from ..content.booking import IBooking
from ..vocabularies.utils import get_vocab_term
from datetime import date
from dateutil.relativedelta import MO
from dateutil.relativedelta import relativedelta
from dateutil.relativedelta import SU
from plone import api
from pprint import pprint
from Products.Five.browser import BrowserView
from zope.interface import implementer
from zope.interface import Interface

import zope.schema


class IBookingsView(Interface):
    """Marker Interface for IBookingsView"""


@implementer(IBookingsView)
class BookingsView(BrowserView):
    def __call__(self):
        self.date = date.today()
        rdate = self.request.get("date")
        if rdate:
            self.date = date.fromisoformat(rdate)
        week_dates = self.get_week_dates()
        pprint(week_dates)
        current_week_bookings = self.find_bookings(
            week_dates["current_week"][0],
            week_dates["current_week"][1],
        )
        self.current_week_bookings = self.resolve_vocabularies(current_week_bookings)
        self.bookings_by_resource = self.get_bookings_by_resource(self.current_week_bookings)
        pprint(self.bookings_by_resource)
        return self.index()

    def find_bookings(self, week_start, week_end):
        bookings = api.content.find(
            context=self.context,
            portal_type="Booking",
            start={
                "query": week_end,
                "range": "max",
            },
            end={
                "query": week_start,
                "range": "min",
            },
            order_by=['day', 'timeslot']
        )
        pprint(bookings)
        return bookings

    def resolve_vocabularies(self, bookings):
        resolved_bookings = []
        fields = zope.schema.getFields(IBooking)
        for brain in bookings:
            booking = brain.getObject()
            booking_info = {}
            booking_info["resource"] = get_vocab_term(
                booking, fields["resource"], booking.resource
            )["title"]
            booking_info["timeslot"] = get_vocab_term(
                booking, fields["timeslot"], booking.timeslot
            )["title"]
            booking_info["day"] = booking.day.isoformat()
            booking_info["url"] = booking.absolute_url()
            resolved_bookings.append(booking_info)
        return resolved_bookings

    def get_bookings_by_resource(self, bookings):
        bookings_by_room = {}
        for booking in bookings:
            if booking['resource'] not in bookings_by_room:
                bookings_by_room[booking['resource']] = []
            bookings_by_room[booking['resource']].append(booking)
        return bookings_by_room

    def get_week_dates(self):
        today = self.date
        current_week_start = today + relativedelta(weekday=MO(-1))
        current_week_end = today + relativedelta(weekday=SU)
        next_week_start = today + relativedelta(weekday=MO(+1))
        next_week_end = today + relativedelta(weekday=SU(+2))
        nextnext_week_start = today + relativedelta(weekday=MO(+2))
        nextnext_week_end = today + relativedelta(weekday=SU(+3))
        return {
            "current_week": (current_week_start, current_week_end),
            "next_week": (next_week_start, next_week_end),
            "nextnext_week": (nextnext_week_start, nextnext_week_end),
        }
