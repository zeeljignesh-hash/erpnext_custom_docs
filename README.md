# ERPNext Custom Document Formats

A complete Frappe/ERPNext custom app that adds professional print formats and
custom fields for all major business documents.

## Documents Covered

| Module     | Document Types                                                   |
|------------|------------------------------------------------------------------|
| Sales      | Quotation, Sales Order, Sales Invoice, Delivery Note             |
| Purchase   | Request for Quotation, Purchase Order, Purchase Invoice, Receipt |
| Finance    | Credit Note, Debit Note, Payment Entry                           |
| Inventory  | Stock Transfer, Goods Receipt Note (GRN)                         |

## Installation

```bash
# 1. Go to your bench directory
cd /home/frappe/frappe-bench

# 2. Get the app
bench get-app erpnext_custom_docs /path/to/erpnext_custom_docs
# OR copy this folder into apps/ manually

# 3. Install on your site
bench --site your-site.local install-app erpnext_custom_docs

# 4. Run migrations
bench --site your-site.local migrate

# 5. Clear cache
bench --site your-site.local clear-cache

# 6. Restart
bench restart
```

## What Gets Installed

- **Print Formats** — Professional Jinja2 HTML templates for every document type
- **Custom Fields** — Extra fields (e.g. VAT Reg No, Authorized Signatory, Bank Details)
- **Fixtures** — Auto-loads print formats and custom fields on install
- **Hooks** — Overrides default print format per doctype
