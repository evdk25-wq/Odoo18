{
    "name": "Mini CRM",
    "version": "1.0.0",
    "category": "Sales/CRM",
    "summary": "Simple CRM for managing commercial opportunities",
    "description": """
        Mini CRM
        ========

        Gestion simple des clients et opportunités commerciales.
    """,
    "author": "Edwin",
    "license": "LGPL-3",
    "depends": ["base"],
    "data": [
        "security/ir.model.access.csv",
        "views/opportunity_views.xml",
        "views/res_partner_views.xml"

    ],
    "installable": True,
    "application": True,
}
