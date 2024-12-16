def execute(filters=None):
	if filters.date_from_filter and filters.date_to_filter:
		if filters.date_from_filter > filters.date_to_filter:
			frappe.throw("The 'From Date' ({}) must be before the 'To Date' ({})".format(filters.date_from_filter, filters.date_to_filter))
	if filters.date_from_filter == None:
		filters.date_from_filter = "2000-01-01"
	if filters.date_to_filter == None:
		filters.date_to_filter = frappe.datetime.get_today()
	conditions = " WHERE creation BETWEEN '" + filters.date_from_filter + "' AND '" + filters.date_to_filter + "'"
	if filters.get("name_filter"):
		name = filters.get("name_filter")
		conditions += f" AND user = '{name}'"
	# if len(filters.get("subject_filter")) > 0:
		# subject = ','.join("'{0}'".format(x) for x in filters.get("subject_filter"))
		# conditions += " AND subject IN (" + subject + ")"
	columns = [
		{'fieldname':'name','label':'Name','width':'250'},
		{'fieldname':'full_name','label':'Full Name','width':'250'},
		{'fieldname':'subject','label':'Subject','width':'350'},
		{'fieldname':'status','label':'Status','width':'100'},
		{'fieldname':'creation','label':'Creation','width':'250'}
	]
	data = []
	users = frappe.get_list("User", fields=["name","full_name","'0' AS indent"], filters=[{"name":filters.get("name_filter")}], order_by='full_name ASC')
	for user in users:
		user["has_value"] = True
		data.append(user)
		activities = frappe.db.sql("SELECT subject, status, creation, '1' AS indent FROM `tabActivity Log`" + conditions, as_dict=1)
		for activity in activities:
			activity["has_value"] = False
			data.append(activity)
	return columns, data
