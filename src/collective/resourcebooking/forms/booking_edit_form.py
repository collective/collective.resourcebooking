# from collective.resourcebooking import _
from collective.resourcebooking.forms.booking_default_add_form import ADDFORM_FIELDS
from plone.dexterity.browser import edit
from zope.interface import implementer
from zope.interface import Interface


class IBookingEditForm(Interface):
    """ """


@implementer(IBookingEditForm)
class BookingEditForm(edit.DefaultEditForm):
    # portal_type = "Booking"
    addform_fields = ADDFORM_FIELDS

    def updateFieldsFromSchemata(self):
        super().updateFieldsFromSchemata()
        # filter out fields which are in addform_fields
        for field_name in self.fields:
            if field_name == "title":
                continue
            if field_name == "description":
                continue
            if field_name in self.addform_fields:
                self.fields[field_name].mode = "display"
