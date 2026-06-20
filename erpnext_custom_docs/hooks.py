app_name = "erpnext_custom_docs"
app_title = "ERPNext Custom Documents"
app_publisher = "Your Company"
app_description = "Professional print formats for all ERPNext document types"
app_email = "admin@yourcompany.com"
app_license = "MIT"
app_version = "1.0.0"

# Explicitly define dependencies using NPM-style semver
required_apps = [
    "frappe >=15.0.0 <16.0.0",
    "erpnext >=15.0.0 <16.0.0"
]

# Fixtures loaded on bench migrate
fixtures = [
    {
        "doctype": "Print Format",
        "filters": [["module", "=", "ERPNext Custom Docs"]],
    },
    {
        "doctype": "Custom Field",
        "filters": [["module", "=", "ERPNext Custom Docs"]],
    },
]
