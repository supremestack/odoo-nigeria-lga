# -*- coding: utf-8 -*-
{
    'name': 'Nigeria States and Local Governments',
    'version': '18.0.1.0.0',
    'category': 'Localization',
    'sequence': 100,
    'summary': 'Complete Nigerian States and LGA Management System',
    'description': """
Nigeria States and Local Governments Module by Supreme Stack
=============================================================

Comprehensive management system for Nigerian administrative divisions.

Key Features:
-------------
* All 36 Nigerian states + Federal Capital Territory (FCT)
* Complete 774 Local Government Areas (LGAs)
* 6 Geopolitical zones classification
* Integration with Odoo contacts
* Modern responsive UI with dashboards
* RESTful API endpoints
* Import/Export capabilities
* OCA compliant structure

Developed by Supreme Stack
---------------------------
Enterprise Odoo Solutions for Africa
    """,
    'author': 'Supreme Stack',
    'company': 'Supreme Stack',
    'maintainer': 'Supreme Stack',
    'website': 'https://supremestack.net',
    'support': 'support@supremestack.net',
    'license': 'LGPL-3',
    'depends': [
        'base',
        'web',
        'contacts',
        'mail',
    ],
    'data': [
        'security/nigeria_lga_security.xml',
        'security/ir.model.access.csv',
        'views/nigeria_state_views.xml',
        'views/nigeria_lga_views.xml',
        'views/res_partner_views.xml',
        'views/menu_views.xml',
    ],
    'assets': {
        'web.assets_backend': [
            'nigeria_lga/static/src/scss/nigeria_lga.scss',
            'nigeria_lga/static/src/js/nigeria_dashboard.js',
        ],
    },
    'installable': True,
    'application': True,
    'auto_install': False,
}
