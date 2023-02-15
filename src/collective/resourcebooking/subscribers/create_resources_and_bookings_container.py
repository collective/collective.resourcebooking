# -*- coding: utf-8 -*-
from plone import api
from collective.resourcebooking import logger
from Acquisition import aq_inner


def handler(obj, event):
    """Event handler"""
    container = aq_inner(event.object)
    bookings = api.content.create(
        container=container, type="Bookings", id="bookings", title="Bookings"
    )
    resources = api.content.create(
        container=container, type="Resources", id="resources", title="Resources"
    )
    logger.info(f"Subscriber created bookings and resources containers in : {obj.absolute_url()}")
