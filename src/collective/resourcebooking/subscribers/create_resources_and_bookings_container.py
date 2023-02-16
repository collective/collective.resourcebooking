# -*- coding: utf-8 -*-
from Acquisition import aq_inner
from collective.resourcebooking import logger
from plone import api


def handler(obj, event):
    """Event handler"""
    container = aq_inner(event.object)
    api.content.create(
        container=container, type="Bookings", id="bookings", title="Bookings"
    )
    api.content.create(
        container=container, type="Resources", id="resources", title="Resources"
    )
    logger.info(
        f"Subscriber created bookings and resources containers in : {obj.absolute_url()}"
    )
