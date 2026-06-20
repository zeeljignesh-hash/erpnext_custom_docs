import frappe


def after_install():
    """Set default print formats for all covered doctypes."""
    mappings = {
        "Quotation":          "Custom Quotation",
        "Sales Order":        "Custom Sales Order",
        "Sales Invoice":      "Custom Sales Invoice",
        "Delivery Note":      "Custom Delivery Note",
        "Purchase Order":     "Custom Purchase Order",
        "Purchase Invoice":   "Custom Purchase Invoice",
        "Payment Entry":      "Custom Payment Entry",
        "Stock Entry":        "Custom Stock Transfer",
        "Purchase Receipt":   "Custom Goods Receipt Note",
        "Supplier Quotation": "Custom RFQ",
    }
    for doctype, fmt in mappings.items():
        if frappe.db.exists("Print Format", fmt):
            frappe.db.set_value("DocType", doctype, "default_print_format", fmt)
            frappe.db.commit()
