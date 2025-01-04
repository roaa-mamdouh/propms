# Import frappe for database and validation operations
import frappe
from frappe.model.document import Document

class DealIsDone(Document):
    def validate(self):
        # Ensure the selected reservation form has the status 'Approved'
        if self.reservation_form:
            reservation_status = frappe.db.get_value("Reservation form", self.reservation_form, "status")
            if reservation_status != "Approved":
                frappe.throw(f"Only 'Approved' Reservation Forms can be selected. The selected Reservation Form '{self.reservation_form}' has status '{reservation_status}'.")
