# -*- coding: utf-8 -*-

# from collective.resourcebooking import _
from datetime import date
from dateutil.relativedelta import MO
from dateutil.relativedelta import relativedelta
from dateutil.relativedelta import SU
from plone import api
from Products.Five.browser import BrowserView
from zope.interface import Interface


class IBookingsView(Interface):
    """Marker Interface for IBookingsView"""


class BookingsView(BrowserView):
    def __call__(self):
        week_dates = self.get_week_dates()
        print(week_dates)
        self.current_week_bookings = self.find_bookings(
            week_dates["current_week"][0],
            week_dates["current_week"][1],
        )
        self.next_week_bookings = self.find_bookings(
            week_dates["next_week"][0],
            week_dates["next_week"][1],
        )
        return self.index()

    def find_bookings(self, week_start, week_end):
        bookings = api.content.find(
            container=self.context,
            portal_type="Booking",
            start={
                "query": week_end,
                "range": "max",
            },
            end={
                "query": week_start,
                "range": "min",
            },
        )
        return bookings

    def get_week_dates(self):
        today = date.today()
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
