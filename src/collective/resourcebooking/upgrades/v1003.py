# -*- coding: utf-8 -*-

from . import logger
from .base import reload_gs_profile


# from plone import api


def upgrade(setup_tool=None):
    """ """
    logger.info(
        "Running upgrade (Python): load config to enable plone.eventbasic behavior for Booking CT"
    )
    reload_gs_profile(setup_tool)
