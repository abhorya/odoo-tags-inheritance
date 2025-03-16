{
    'name': 'Tags Inheritance',
    'version': '1.0',
    'category': 'Sales/CRM',
    'summary': 'Extends tag functionality for customers, vendors and products',
    'depends': [
        'base',
        'crm',
        'sales_team',
        'product',
    ],
    'data': [
        'security/tag_security.xml',
        'security/ir.model.access.csv',
        'views/crm_tag_tree_inherit.xml',
        'views/res_partner_views.xml',
        'views/res_users_views.xml',
        'views/product_template_views.xml',
        'views/product_tag_form_view.xml',
        'views/account_tag_views.xml',
        'views/tag_dashboard_views.xml',
    ],
    'images': [
        'static/description/icon.png',
        'static/description/screenshot1.png',
        'static/description/screenshot2.png',
        'static/description/screenshot3.png',
        'static/description/screenshot4.png',
        'static/description/screenshot5.png',
        'static/description/screenshot6.png',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
    'price': 99.99,
    'currency': 'EUR',
    'license': 'OPL-1',
    'author': 'Sabry Youssef',
    'website': 'https://www.linkedin.com/in/sabry-youssef/',
    'support': 'vendorah2@gmail.com',
    'maintainer': 'Sabry Youssef (Phone: +20 1000059085)',
    'description': """
Tags Inheritance
===============

Enhanced Tag Management for Customers, Vendors, and Products
-----------------------------------------------------------

This module enhances Odoo's filtering and categorization system by allowing users to assign Customer Tags, Vendor Tags, and Product Tags to different entities. It provides improved data organization and faster access to important records.

Key Features:
------------
* Enhanced Tag Management - Manage and assign Customer, Vendor, and Product Tags
* Advanced Filtering - Use powerful search filters based on tags
* Group by Tags - Organize contacts, users, and products by grouping them based on assigned tags
* Tag Dashboard - Access a dedicated dashboard for comprehensive tag management
* Seamless Integration - Works perfectly with Odoo CRM, Sales, and Inventory modules

For more information, please visit the module description page.
    """,
}
