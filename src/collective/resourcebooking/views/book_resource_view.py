# -*- coding: utf-8 -*-

from Products.Five.browser import BrowserView
from zope.interface import implementer
from zope.interface import Interface


class IBookResourceView(Interface):
    """Marker Interface for IBookResourceView"""


@implementer(IBookResourceView)
class BookResourceView(BrowserView):
    def __call__(self):
        template = """<li class="heading" i18n:translate="">
          Sample View
        </li>"""
        return template
