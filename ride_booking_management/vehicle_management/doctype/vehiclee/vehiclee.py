# Copyright (c) 2026, Dakshit and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document
from frappe.utils import today


class Vehiclee(Document):
	def validate(self):
		if self.registration_expiry and self.registration_expiry < today():
			frappe.throw("Vehicle registration expired")

		if self.assigned_driver:
			exists = frappe.db.exists("Vehiclee", {
				"assigned_driver": self.assigned_driver,
				"name": ["!=", self.name]
			})
			if exists:
				frappe.throw("Driver already assigned to another vehicle")
