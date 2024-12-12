import frappe
from datetime import datetime

@frappe.whitelist()
def get_target_data():
    current_month = datetime.now().strftime("%m")
    target_doc_name = f"{current_month}-Target"
    target_doc = frappe.get_doc("Target", target_doc_name)

    # Prepare the data
    labels = ["Target", "Reservations", "Done Deal"]
    values = [
        target_doc.target,
        target_doc.reservations,
        target_doc.done_deal
    ]
    
    return {
        "labels": labels,
        "datasets": [{
            "name": "Current Month Data",
            "values": values
        }]
    }

