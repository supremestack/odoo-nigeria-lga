# Nigerian States & LGAs Module for Odoo

[![License: LGPL-3](https://img.shields.io/badge/License-LGPL%203.0-blue.svg)](https://www.gnu.org/licenses/lgpl-3.0)
[![Odoo Version](https://img.shields.io/badge/Odoo-18.0-875A7B.svg)](https://www.odoo.com/)
[![Maintenance](https://img.shields.io/badge/Maintained%3F-yes-green.svg)](https://github.com/supremestack)

## 📍 Overview

The **l10n_ng_states** module provides comprehensive Nigerian geographical data for Odoo 18, automatically populating all Nigerian states and Local Government Areas (LGAs) in your Odoo instance. This localization module is essential for businesses operating in Nigeria that need accurate address management and location-based reporting.

## ✨ Features

- **Complete State Coverage**: All 36 Nigerian states plus the Federal Capital Territory (FCT)
- **Comprehensive LGA Data**: All 774 Local Government Areas properly mapped to their respective states
- **Seamless Integration**: Works with Odoo's standard address fields
- **No Configuration Required**: Install and use immediately
- **Standardized Data**: Consistent naming conventions across all locations

## 📋 Requirements

- Odoo 18.0 or higher
- Base module (included in Odoo by default)

## 🚀 Installation

### Method 1: From Odoo Apps

1. Navigate to **Apps** in your Odoo instance
2. Search for "Nigeria LGAs & States"
3. Click **Install**

### Method 2: Manual Installation

1. Download the module to your Odoo addons directory:
   ```bash
   cd /path/to/odoo/addons
   git clone https://github.com/supremestack/l10n_ng_states.git
   ```

2. Update the addons list:
   - Go to **Apps** → **Update Apps List**
   - Or restart Odoo with `--update=all` flag

3. Install the module:
   - Search for "Nigeria LGAs & States" in Apps
   - Click **Install**

## 🎯 Usage

Once installed, the module automatically:

1. **Populates State Fields**: All Nigerian states become available in the state dropdown when Nigeria is selected as the country

2. **Provides LGA Selection**: City/LGA fields will show appropriate Local Government Areas based on the selected state

3. **Enhances Address Forms**: 
   - In partner/contact forms
   - In company settings
   - In delivery addresses
   - In billing addresses

### Example Usage in Forms

When creating a new contact or partner:
1. Select **Country**: Nigeria
2. Select **State**: e.g., Lagos
3. Select **City/LGA**: e.g., Ikeja
4. Complete other address fields as needed

## 📊 Data Structure

### States Organization

The module organizes Nigerian states by geopolitical zones:

#### North Central (7 states)
- Benue (BEN)
- Kogi (KOG)
- Kwara (KWR)
- Nasarawa (NAS)
- Niger (NGR)
- Plateau (PLT)
- Federal Capital Territory (FCT)

#### North East (6 states)
- Adamawa (ADM)
- Bauchi (BAU)
- Borno (BOR)
- Gombe (GOM)
- Taraba (TAR)
- Yobe (YOB)

#### North West (7 states)
- Jigawa (JIG)
- Kaduna (KAD)
- Kano (KAN)
- Katsina (KTS)
- Kebbi (KEB)
- Sokoto (SKT)
- Zamfara (ZAM)

#### South East (5 states)
- Abia (ABI)
- Anambra (ANA)
- Ebonyi (EBN)
- Enugu (ENU)
- Imo (IMO)

#### South South (6 states)
- Akwa Ibom (AKW)
- Bayelsa (BAY)
- Cross River (CRS)
- Delta (DEL)
- Edo (EDO)
- Rivers (RIV)

#### South West (6 states)
- Ekiti (EKT)
- Lagos (LAG)
- Ogun (OGN)
- Ondo (OND)
- Osun (OSU)
- Oyo (OYO)

## 🔧 Technical Details

### Module Structure
```
l10n_ng_states/
├── __init__.py                    # Module initialization
├── __manifest__.py                 # Module manifest file
├── README.md                       # This file
├── data/
│   ├── nigeria_states.xml         # States data (37 records)
│   └── res_city_data.xml          # LGAs data (774 records)
└── static/
    └── description/
        └── icon.png                # Module icon (optional)
```

### Data Models Used

- **res.country.state**: Extended to include Nigerian states
- **res.city**: Extended to include Nigerian LGAs
- **base.ng**: Reference to Nigeria country record

### XML Record Structure

States are defined as:
```xml
<record id="state_ng_lagos" model="res.country.state">
    <field name="name">Lagos</field>
    <field name="code">LAG</field>
    <field name="country_id" ref="base.ng"/>
</record>
```

LGAs are defined as:
```xml
<record id="city_lagos_ikeja" model="res.city">
    <field name="name">Ikeja</field>
    <field name="state_id" ref="state_ng_lagos"/>
    <field name="country_id" ref="base.ng"/>
</record>
```

## 🧪 Testing

To verify the installation:

1. Go to **Contacts** → **Create**
2. Set Country to **Nigeria**
3. Check that State dropdown shows all Nigerian states
4. Select a state and verify LGAs appear in City field

## 🤝 Contributing

We welcome contributions! To contribute:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

### Reporting Issues

If you find any issues or discrepancies in the LGA data:
1. Check if the issue exists in the latest version
2. Create an issue with:
   - State name
   - LGA name (if applicable)
   - Description of the issue
   - Expected vs actual behavior

## 📜 License

This module is licensed under the LGPL-3.0 License. See the [LICENSE](https://www.gnu.org/licenses/lgpl-3.0) file for details.

## 👥 Credits

### Authors
* Supreme Stack Systems Limited

### Contributors
* Supreme Stack Development Team

### Maintainer

<img src="https://supremestack.net/logo.png" alt="Supreme Stack Systems" width="200"/>

This module is maintained by Supreme Stack Systems Limited.

Website: [https://supremestack.net](https://supremestack.net)

For support, customization, or Odoo implementation services, contact us at:
- Email: info@supremestack.net
- Phone: +234 XXX XXX XXXX

## 📈 Changelog

### Version 18.0.1.0.0 (2025-01)
- Initial release for Odoo 18
- Complete Nigerian states data (36 + FCT)
- Complete LGAs data (774 LGAs)
- Full compatibility with Odoo 18.0

## 🗺️ Roadmap

- [ ] Add ward-level data for major cities
- [ ] Include postal codes for all LGAs
- [ ] Add geolocation coordinates for mapping
- [ ] Create views for geographical reports
- [ ] Add data validation rules
- [ ] Include alternative LGA names/spellings

## ⚠️ Known Issues

- None reported at this time

## 💡 Tips

1. **Performance**: The module loads all data on installation. This is a one-time process and doesn't affect runtime performance.

2. **Updates**: When updating the module, new LGAs or corrections will be automatically applied.

3. **Customization**: You can extend this module to add custom fields to states or LGAs by inheriting the models.

4. **Integration**: Works seamlessly with:
   - Accounting (for tax zones)
   - Sales (for delivery zones)
   - HR (for employee locations)
   - Inventory (for warehouse locations)

## 🙏 Acknowledgments

- Odoo Community for the framework
- Nigerian Government for official LGA listings
- Open Source Community for continuous support

---

**Note**: This module is provided as-is. While we strive for accuracy, please verify critical geographical data with official sources when necessary.
