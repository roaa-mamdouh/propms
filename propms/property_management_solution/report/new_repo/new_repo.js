frappe.query_reports["Script Report Tutorial"] = {
	"treeView": true,
	"name_field": "name",
	"parent_field": "name",
	"initial_depth": 1,			//The level to which the initial rendering will expand to
	//onload: function () {
		//var filter = frappe.query_report.get_filter("name_filter");
		//if (frappe.user.has_role("Administrator") || frappe.user.has_role("System Manager")) {
			//filter.set_input("Goofy");
		//} else {
			//filter.set_input(frappe.user.name);
		//};
		//filter.refresh();
		//frappe.query_report.refresh();
	//},
	"filters": [
		{
			fieldname: "name_filter",
			label: "Name Filter",
			fieldtype: "Link",
			options: "User",
			reqd: 1,
			default: (frappe.user.has_role("Administrator") || frappe.user.has_role("System Manager")) ? "" : frappe.user.name,
			hidden: !(frappe.user.has_role("Administrator") || frappe.user.has_role("System Manager")),
			on_change: function(query_report){
				query_report.set_filter_value('subject_filter', []);
				query_report.refresh();
			},
		},
		{
			fieldname: "subject_filter",
			label: "Subject Filter",
			fieldtype: "MultiSelectList",
			get_data: function(txt) {
				if (frappe.query_report.get_filter_value('name_filter')) {
					var name = frappe.query_report.get_filter_value("name_filter");
					return frappe.db.get_list("Activity Log", {fields: ['subject AS value', 'subject AS label', 'subject AS description'], filters: {"user": name}, distinct: 1, order_by: "subject"});
					//return frappe.db.get_link_options("Activity Log", txt, {"user":name});
				}
				else {
					return [];
				};
			},
			on_change: function(query_report) {
				query_report.refresh();
			},
		},
		{
			fieldname: "date_from_filter",
			label: "Date From Filter",
			fieldtype: "Date",
			default: frappe.datetime.add_months(frappe.datetime.get_today(), -1)
		},
		{
			fieldname: "date_to_filter",
			label: "Date To Filter",
			fieldtype: "Date",
			default: frappe.datetime.get_today()
		}
	],
};
