def after_save(doc, method):
    # Check if 'for_cancellation' is still "Available" and 'status' is set
    if doc.for_cancellation == "Available" and doc.status:
        # Set 'for_cancellation' to the current 'status' if it is a valid option
        if doc.status in doc.meta.get_field('for_cancellation').options.split('\n'):
            doc.for_cancellation = doc.status
            doc.db_update()  # Save the updated value to the database

