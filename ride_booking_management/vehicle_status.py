import frappe

def reserve_vehicle(doc, method):
    if doc.status == "Confirmed" and doc.vehicle:
        frappe.db.set_value(
            "Vehiclee",
            doc.vehicle,
            "status",
            "In Service"
        )
def release_vehicle(doc, method):
    if doc.vehicle:
        frappe.db.set_value(
            "Vehiclee",
            doc.vehicle,
            "status",
            "Available"
        )

def check_vehicle_availability(doc, method):
    if doc.docstatus == 1:
        return
    vehicle_status = frappe.db.get_value(
        "Vehiclee",
        doc.vehicle,
        "status"
    )

    if vehicle_status != "Available":
        frappe.throw(f"Vehicle {doc.vehicle} not available")