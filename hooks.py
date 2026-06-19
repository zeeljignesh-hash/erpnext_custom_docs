app_name = "erpnext_custom_docs"
app_title = "ERPNext Custom Documents"
app_publisher = "Your Company"
app_description = "Professional print formats and custom fields for all ERPNext document types"
app_email = "admin@yourcompany.com"
app_license = "MIT"

# ---------------------------------------------------------------------------
# Fixtures — these JSON files are loaded on `bench migrate`
# ---------------------------------------------------------------------------
fixtures = [
    # Custom fields added to standard doctypes
    {
        "doctype": "Custom Field",
        "filters": [["module", "=", "ERPNext Custom Docs"]],
    },
    # All print formats defined in this app
    {
        "doctype": "Print Format",
        "filters": [["module", "=", "ERPNext Custom Docs"]],
    },
]

# ---------------------------------------------------------------------------
# Default print format per doctype
# Set these after installing so every new document uses the custom format.
# ---------------------------------------------------------------------------
default_print_format = {
    "Quotation":         "Custom Quotation",
    "Sales Order":       "Custom Sales Order",
    "Sales Invoice":     "Custom Sales Invoice",
    "Delivery Note":     "Custom Delivery Note",
    "Purchase Order":    "Custom Purchase Order",
    "Purchase Invoice":  "Custom Purchase Invoice",
    "Payment Entry":     "Custom Payment Entry",
    "Stock Entry":       "Custom Stock Transfer",
    "Purchase Receipt":  "Custom Goods Receipt Note",
    "Supplier Quotation":"Custom RFQ",
}

# ---------------------------------------------------------------------------
# CSS included in all print formats (referenced via /assets/...)
# ---------------------------------------------------------------------------
# app_include_css = ["/assets/erpnext_custom_docs/css/print_common.css"]
