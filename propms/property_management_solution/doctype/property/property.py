# -*- coding: utf-8 -*-
# Copyright (c) 2018, Aakvatech and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
from frappe.utils.nestedset import NestedSet
import frappe


class Property(NestedSet):
    nsm_parent_field = "parent_property"

    def on_trash(self, allow_root_deletion=True):
        super().on_trash(allow_root_deletion)

    def autoname(self):
        # If it is a project
        if self.is_group:
            # Use the Parent Property name as the document name
            self.name = frappe.db.get_value("Property", self.parent_property, "name") if self.parent_property else "Unnamed Project"
        else:
            # If not a project, append the 'name1' field to the Parent Property name
            parent_name = frappe.db.get_value("Property", self.parent_property, "name") if self.parent_property else "Unnamed Property"
            self.name = f"{parent_name}-{self.name1}" if self.name1 else parent_name

@frappe.whitelist()
def add_node():
    from frappe.desk.treeview import make_tree_args

    args = frappe.form_dict
    args = make_tree_args(**frappe.form_dict)

    if args["is_root"]:
        args["parent_property"] = None

    doc = frappe.get_doc(args)

    doc.save()
