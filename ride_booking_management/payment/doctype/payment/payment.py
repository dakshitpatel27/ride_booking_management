# Copyright (c) 2026, Dakshit and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class Payment(Document):
	def validate(self):
		completed = frappe.db.exists("Payment", {
			"ride_booking": self.ride_booking,
			"status": "Completed",
			"name": ["!=", self.name]
		})
		if completed:
			frappe.throw("Payment already completed")


