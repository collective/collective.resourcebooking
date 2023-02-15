# from collective.resourcebooking import _
from plone import schema
from plone.autoform.form import AutoExtensibleForm
from plone.dexterity.browser import add
from z3c.form import button
from z3c.form import form
from zope.interface import Interface


ADDFORM_FIELDS = [
    "title",
    "ressource",
]


class BookingDefaultAddForm(add.DefaultAddForm):
    autoGroups = False
    portal_type = "Booking"

    addform_fields = ADDFORM_FIELDS

    def updateFieldsFromSchemata(self):
        super().updateFieldsFromSchemata()

        # we do not want the extra groups...
        self.groups = ()

        # filter out fields which are not in addform_fields
        for field_name in self.fields:
            if field_name not in self.addform_fields:
                self.fields = self.fields.omit(field_name)

    def nextURL(self):
        if self.immediate_view is not None:
            return "{:s}/@@edit".format("/".join(self.immediate_view.split("/")[:-1]))
        else:
            return self.context.absolute_url()


class BookingDefaultAddView(add.DefaultAddView):
    form = BookingDefaultAddForm
