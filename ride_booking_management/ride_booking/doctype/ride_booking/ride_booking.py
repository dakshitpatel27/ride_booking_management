import frappe
import json
from frappe.model.document import Document
from ride_booking_management.distance import calculate_distance


class RideBooking(Document):
    def validate(self):
        self.set_distance()
        self.set_fare()
        self.validate_driver()

    def set_distance(self):
        if self.pickup_location and self.drop_location:
            self.distance = calculate_distance(
                self.pickup_location,
                self.drop_location
            )

    def set_fare(self):
        if self.distance:
            base_fare = 40
            per_km_rate = 12
            self.fare_amount = base_fare + (self.distance * per_km_rate)

    def validate_driver(self):
        if self.assigned_driver:
            driver = frappe.get_doc("Driverr", self.assigned_driver)
            if driver.status != "Active":
                frappe.throw("Driver not active")
