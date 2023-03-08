# -*- coding: utf-8 -*-

from Products.Five.browser import BrowserView
from zope.interface import implementer
from zope.interface import Interface


class ICancelResourceBookingView(Interface):
    """Marker Interface for ICancelResourceBookingView"""


@implementer(ICancelResourceBookingView)
class CancelResourceBookingView(BrowserView):
    def __call__(self):
        template = """<li class="heading" i18n:translate="">
          Sample View
        </li>"""
        return template
