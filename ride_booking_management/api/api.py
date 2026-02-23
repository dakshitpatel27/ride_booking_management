import frappe

@frappe.whitelist(allow_guest=True)
def create_ride(customer_name, pickup, drop):

    ride = frappe.get_doc({
        "doctype": "Ride Booking",
        "customer_name": customer_name,
        "customer_email" : "gajiparadakshit@gmail.com",
        "pickup_location": pickup,
        "drop_location": drop,
        "assigned_driver":"Driver 1",
        "distance": 10,
        "fare_amount": 150,
        "status": "Draft"
    })

    ride.insert(ignore_permissions=True)
    frappe.db.commit()

    return {
        "ride_id": ride.name,   
        "pickup_location": ride.pickup_location,
        "drop_location": ride.drop_location,
        "status": ride.status
    }