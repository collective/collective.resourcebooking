# from collective.resourcebooking import _
from plone import schema
from plone.autoform.form import AutoExtensibleForm
from z3c.form import button
from z3c.form import form
from zope.interface import Interface


class IBookingDefaultAddForm(Interface):
    """Schema Interface for IBookingDefaultAddForm
    Define your form fields here.
    """

    name = schema.TextLine(
        title="Your name",
    )


class BookingDefaultAddForm(AutoExtensibleForm, form.EditForm):
    schema = IBookingDefaultAddForm
    ignoreContext = True

    label = "What's your name?"
    description = "Simple, sample form"

    @button.buttonAndHandler("Ok")
    def handleApply(self, action):
        data, errors = self.extractData()
        if errors:
            self.status = self.formErrorsMessage
            return

        # Do something with valid data here

        changes = self.applyChanges(data)
        # Set status on this form page
        # (this status message is not bind to the session and does not go thru redirects)
        if changes:
            self.status = "Settings saved"

    @button.buttonAndHandler("Cancel")
    def handleCancel(self, action):
        """User canceled. Redirect back to the front page."""
