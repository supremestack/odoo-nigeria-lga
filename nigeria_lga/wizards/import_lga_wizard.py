# ===================================================================
# nigeria_lga/wizards/import_lga_wizard.py
# ===================================================================

# -*- coding: utf-8 -*-
# Copyright 2025 Supreme Stack
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl).

from odoo import api, fields, models, _
from odoo.exceptions import UserError
import base64
import csv
import io


class ImportLGAWizard(models.TransientModel):
    """Wizard for importing LGA data from CSV"""
    _name = 'import.lga.wizard'
    _description = 'Import LGA Wizard'
    
    file_data = fields.Binary(
        string='CSV File',
        required=True,
        help='Select CSV file containing LGA data'
    )
    file_name = fields.Char(string='File Name')
    delimiter = fields.Selection([
        (',', 'Comma'),
        (';', 'Semicolon'),
        ('\t', 'Tab'),
        ('|', 'Pipe'),
    ], string='Delimiter', default=',', required=True)
    import_type = fields.Selection([
        ('states', 'States Only'),
        ('lgas', 'LGAs Only'),
        ('both', 'States and LGAs'),
    ], string='Import Type', default='both', required=True)
    update_existing = fields.Boolean(
        string='Update Existing Records',
        default=False,
        help='If checked, existing records will be updated'
    )
    
    def action_import(self):
        """Import data from CSV file"""
        self.ensure_one()
        
        if not self.file_name.endswith('.csv'):
            raise UserError(_('Please upload a CSV file.'))
        
        # Decode file
        csv_data = base64.b64decode(self.file_data)
        data_file = io.StringIO(csv_data.decode("utf-8"))
        
        # Read CSV
        reader = csv.DictReader(data_file, delimiter=self.delimiter)
        
        if self.import_type == 'states':
            return self._import_states(reader)
        elif self.import_type == 'lgas':
            return self._import_lgas(reader)
        else:
            return self._import_both(reader)
    
    def _import_states(self, reader):
        """Import states data"""
        imported_count = 0
        errors = []
        
        for row in reader:
            try:
                # Check if state exists
                state = self.env['nigeria.state'].search([
                    ('code', '=', row.get('code', '').upper())
                ], limit=1)
                
                vals = {
                    'name': row.get('name'),
                    'code': row.get('code', '').upper(),
                    'capital': row.get('capital'),
                    'geopolitical_zone': row.get('zone'),
                    'governor_name': row.get('governor', ''),
                    'deputy_governor_name': row.get('deputy_governor', ''),
                    'website': row.get('website', ''),
                }
                
                if state and self.update_existing:
                    state.write(vals)
                elif not state:
                    self.env['nigeria.state'].create(vals)
                
                imported_count += 1
                
            except Exception as e:
                errors.append(f"Row {reader.line_num}: {str(e)}")
        
        return self._prepare_result(imported_count, errors)
    
    def _import_lgas(self, reader):
        """Import LGAs data"""
        imported_count = 0
        errors = []
        
        for row in reader:
            try:
                # Find state
                state = self.env['nigeria.state'].search([
                    '|',
                    ('name', '=', row.get('state_name')),
                    ('code', '=', row.get('state_code', '').upper())
                ], limit=1)
                
                if not state:
                    errors.append(f"Row {reader.line_num}: State not found: {row.get('state_name')}")
                    continue
                
                # Check if LGA exists
                lga = self.env['nigeria.lga'].search([
                    ('name', '=', row.get('lga_name')),
                    ('state_id', '=', state.id)
                ], limit=1)
                
                vals = {
                    'name': row.get('lga_name'),
                    'code': row.get('lga_code', ''),
                    'state_id': state.id,
                    'headquarters': row.get('headquarters', ''),
                    'chairman_name': row.get('chairman', ''),
                    'postal_codes': row.get('postal_codes', ''),
                }
                
                if lga and self.update_existing:
                    lga.write(vals)
                elif not lga:
                    self.env['nigeria.lga'].create(vals)
                
                imported_count += 1
                
            except Exception as e:
                errors.append(f"Row {reader.line_num}: {str(e)}")
        
        return self._prepare_result(imported_count, errors)
    
    def _import_both(self, reader):
        """Import both states and LGAs"""
        # First pass: Import states
        data_file = io.StringIO(base64.b64decode(self.file_data).decode("utf-8"))
        reader = csv.DictReader(data_file, delimiter=self.delimiter)
        result_states = self._import_states(reader)
        
        # Second pass: Import LGAs
        data_file = io.StringIO(base64.b64decode(self.file_data).decode("utf-8"))
        reader = csv.DictReader(data_file, delimiter=self.delimiter)
        result_lgas = self._import_lgas(reader)
        
        return result_states
    
    def _prepare_result(self, imported_count, errors):
        """Prepare result message"""
        message = f"Successfully imported {imported_count} records."
        if errors:
            message += f"\n\nErrors encountered:\n" + "\n".join(errors[:10])
            if len(errors) > 10:
                message += f"\n... and {len(errors) - 10} more errors"
        
        return {
            'type': 'ir.actions.client',
            'tag': 'display_notification',
            'params': {
                'title': _('Import Result'),
                'message': message,
                'type': 'success' if not errors else 'warning',
                'sticky': True,
            }
        }

