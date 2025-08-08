# -*- coding: utf-8 -*-
# Copyright 2025 Supreme Stack
# License LGPL-3.0 or later (https://www.gnu.org/licenses/lgpl).

{
    "name": "Nigeria - States and Local Governments",
    "summary": "Nigerian States and Local Government Areas with optimal data structure",
    "version": "18.0.1.0.0",
    "development_status": "Production/Stable",
    "category": "Localization",
    "website": "https://github.com/supremestack/odoo-nigeria-lga",
    "author": "Supreme Stack",
    "maintainers": ["supremestack"],
    "license": "LGPL-3",
    "application": False,
    "installable": True,
    "depends": [
        "base",
        "base_address_city",
        "contacts",
    ],
    "data": [
        # Country configuration
        "data/res_country_data.xml",
        
        # States - single file (only 37 records)
        "data/res_country_state_data.xml",
        
        # LGAs - split by region for maintainability
        "data/lga/north_central/01_benue.xml",
        "data/lga/north_central/02_fct.xml",
        "data/lga/north_central/03_kogi.xml",
        "data/lga/north_central/04_kwara.xml",
        "data/lga/north_central/05_nasarawa.xml",
        "data/lga/north_central/06_niger.xml",
        "data/lga/north_central/07_plateau.xml",
        
        "data/lga/north_east/01_adamawa.xml",
        "data/lga/north_east/02_bauchi.xml",
        "data/lga/north_east/03_borno.xml",
        "data/lga/north_east/04_gombe.xml",
        "data/lga/north_east/05_taraba.xml",
        "data/lga/north_east/06_yobe.xml",
        
        "data/lga/north_west/01_jigawa.xml",
        "data/lga/north_west/02_kaduna.xml",
        "data/lga/north_west/03_kano.xml",
        "data/lga/north_west/04_katsina.xml",
        "data/lga/north_west/05_kebbi.xml",
        "data/lga/north_west/06_sokoto.xml",
        "data/lga/north_west/07_zamfara.xml",
        
        "data/lga/south_east/01_abia.xml",
        "data/lga/south_east/02_anambra.xml",
        "data/lga/south_east/03_ebonyi.xml",
        "data/lga/south_east/04_enugu.xml",
        "data/lga/south_east/05_imo.xml",
        
        "data/lga/south_south/01_akwa_ibom.xml",
        "data/lga/south_south/02_bayelsa.xml",
        "data/lga/south_south/03_cross_river.xml",
        "data/lga/south_south/04_delta.xml",
        "data/lga/south_south/05_edo.xml",
        "data/lga/south_south/06_rivers.xml",
        
        "data/lga/south_west/01_ekiti.xml",
        "data/lga/south_west/02_lagos.xml",
        "data/lga/south_west/03_ogun.xml",
        "data/lga/south_west/04_ondo.xml",
        "data/lga/south_west/05_osun.xml",
        "data/lga/south_west/06_oyo.xml",
        
        # Views
        "views/res_partner_views.xml",
        "views/res_city_views.xml",
    ],
    "demo": [
        "demo/demo_data.xml",
    ],
}
