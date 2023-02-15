# -*- coding: utf-8 -*-
"""Init and utils."""
from zope.i18nmessageid import MessageFactory
from logging import getLogger


_ = MessageFactory("collective.resourcebooking")


logger = getLogger("collective.resourcebooking")
