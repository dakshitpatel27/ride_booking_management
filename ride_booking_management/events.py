import frappe
from frappe.utils.pdf import get_pdf

def send_ride_completion_email(doc, method):
    if doc.status != "Completed":
        return
    if not doc.customer_email:
        return
    frappe.enqueue(
        "ride_booking_management.events.after_ride_complete",
        ride=doc.name,
        queue="short"
    )

def after_ride_complete(ride):
    doc = frappe.get_doc("Ride Booking", ride)
    html = frappe.get_print(
        "Ride Booking",
        doc.name,
        print_format="Ride Booking"
    )
    pdf = get_pdf(html)
    frappe.sendmail(
        recipients=[doc.customer_email],
        subject=f"Ride Completed - {doc.name}",
        message=f"""
        Dear {doc.customer_name},<br><br>
        Your ride has been successfully completed.<br>
        Please find attached invoice.<br><br>
        Thank you for choosing our service.
        """,
        attachments=[{
            "fname": f"Ride-{doc.name}.pdf",
            "fcontent": pdf
        }],
        now=False
    )
def update_payment_status(doc, method):
    if doc.status != "Completed":
        return
    if not doc.ride_booking:
        return
    current_status = frappe.db.get_value("Ride Booking",doc.ride_booking,"payment_status")
    if current_status == "Paid":
        return
    frappe.db.set_value("Ride Booking",doc.ride_booking,"payment_status","Paid")
    frappe.db.commit()