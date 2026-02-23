# Copyright (c) 2026, Dakshit and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document
from frappe.utils import today

class Driverr(Document):
	def validate(self):
		if self.license_expiry_date and self.license_expiry_date < today():
			frappe.throw("License Expired")

		if self.status == "Active" and not self.assigned_vehicle:
			frappe.throw("Active driver must have vehicle")
