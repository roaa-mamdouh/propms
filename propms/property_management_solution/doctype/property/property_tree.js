frappe.treeview_settings["Property"] = {
	add_tree_node: "propms.property_management_solution.doctype.property.property.add_node",
	filters: [
		{
			fieldname: "developer",
			fieldtype:"Link",
			options: "Developer",
			label: __("Developer"),
		},
	],
	root_label: __("All Property"),
}
