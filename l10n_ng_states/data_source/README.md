# Data Source Documentation

## Structure

This module organizes Nigerian LGA data optimally for maintenance:

### States (37 records)
- Single file: `data/res_country_state_data.xml`
- Organized by geopolitical zone
- ISO 3166-2:NG compliant codes

### LGAs (774 records)
- Split by zone and state: `data/lga/{zone}/{number}_{state}.xml`
- One file per state for easy maintenance
- Includes postal codes where available

## File Organization
data/
├── res_country_state_data.xml  (37 states)
└── lga/
├── north_central/           (7 states, 121 LGAs)
├── north_east/              (6 states, 112 LGAs)
├── north_west/              (7 states, 186 LGAs)
├── south_east/              (5 states, 95 LGAs)
├── south_south/             (6 states, 123 LGAs)
└── south_west/              (6 states, 137 LGAs)
## Maintenance

To update LGA data:
1. Edit the specific state file in `data/lga/{zone}/`
2. Test the module upgrade
3. Commit with message: `[UPD] l10n_ng_states: Update {state} LGAs`

## Data Sources
- Federal Ministry of Information
- National Bureau of Statistics
- INEC (Independent National Electoral Commission)

## Postal Codes
Nigerian postal codes follow the pattern:
- First digit: Region
- Next two digits: Dispatch district
- Last three digits: Post office

Example: Lagos Island - 101001
- 1: Lagos region
- 01: Island dispatch district
- 001: Main post office
