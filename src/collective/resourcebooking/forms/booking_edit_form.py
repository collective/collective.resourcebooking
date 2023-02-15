# from collective.resourcebooking import _
from plone.dexterity.browser import edit
from z3c.form import button
from zope.interface import Interface
from collective.resourcebooking.forms.booking_default_add_form import ADDFORM_FIELDS
from zope.interface import provider, implementer

class IBookingEditForm(Interface):
    """
    """

@implementer(IBookingEditForm)
class BookingEditForm(edit.DefaultEditForm):
    # portal_type = "Booking"
    addform_fields = ADDFORM_FIELDS

    # label = "What's your name?"
    # description = "Simple, sample form"

    def updateFieldsFromSchemata(self):
        super().updateFieldsFromSchemata()
        # filter out fields which are in addform_fields
        for field_name in self.fields:
            if field_name == "title":
                continue
            if field_name in self.addform_fields:
                self.fields[field_name].mode = "display"