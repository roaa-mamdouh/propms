from frappe.model.document import Document
import frappe


class Reservationform(Document):
    pass


@frappe.whitelist()
def update_property_status(property_name, status):
    """
    Update the status of the Property based on the given status.
    """
    try:
    
        # Fetch the Property document
        property_doc = frappe.get_doc("Property", property_name)

        # Check and update the status
        if property_doc.status != status:  # Avoid unnecessary updates
            property_doc.status = status
            property_doc.save()
            frappe.db.commit()  # Commit the transaction

            # Return appropriate response
            if status == "Reserved":
                return "success"
            elif status == "Available":
                return "success"
        else:
            # Return appropriate response for already set status
            if status == "Reserved":
                return "already_reserved"
            elif status == "Available":
                return "already_available"

    except Exception as e:
        # Log the error and return an error message
        frappe.log_error(frappe.get_traceback(), "Error in updating property status")
        frappe.msgprint(f"Error: {str(e)}")  # Debugging line
        return "error"


