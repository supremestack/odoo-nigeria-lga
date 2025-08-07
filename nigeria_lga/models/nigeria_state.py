# -*- coding: utf-8 -*-
# Copyright 2025 Supreme Stack
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl).

from odoo import api, fields, models, _
from odoo.exceptions import ValidationError


class NigeriaState(models.Model):
    """Model for Nigerian States including FCT"""
    _name = 'nigeria.state'
    _description = 'Nigerian State'
    _order = 'name'
    _rec_name = 'name'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    name = fields.Char(string='State Name', required=True, index=True, tracking=True)
    code = fields.Char(string='State Code', size=3, required=True, index=True)
    capital = fields.Char(string='State Capital', required=True)
    geopolitical_zone = fields.Selection([
        ('north_central', 'North Central'),
        ('north_east', 'North East'),
        ('north_west', 'North West'),
        ('south_east', 'South East'),
        ('south_south', 'South South'),
        ('south_west', 'South West'),
    ], string='Geopolitical Zone', required=True, tracking=True)
    
    lga_ids = fields.One2many('nigeria.lga', 'state_id', string='Local Government Areas')
    lga_count = fields.Integer(string='Number of LGAs', compute='_compute_lga_count', store=True)
    population = fields.Integer(string='Population')
    land_area = fields.Float(string='Land Area (km²)')
    
    governor_name = fields.Char(string='Current Governor')
    deputy_governor_name = fields.Char(string='Deputy Governor')
    
    website = fields.Char(string='Official Website')
    active = fields.Boolean(default=True)
    
    _sql_constraints = [
        ('code_unique', 'UNIQUE(code)', 'State code must be unique!'),
        ('name_unique', 'UNIQUE(name)', 'State name must be unique!'),
    ]
    
    @api.depends('lga_ids')
    def _compute_lga_count(self):
        for state in self:
            state.lga_count = len(state.lga_ids)
    
    @api.constrains('code')
    def _check_code(self):
        for record in self:
            if record.code and not record.code.isupper():
                raise ValidationError(_('State code must be in uppercase!'))
            if len(record.code) != 3:
                raise ValidationError(_('State code must be exactly 3 characters!'))
    
    def action_view_lgas(self):
        """Action to view LGAs of this state"""
        self.ensure_one()
        return {
            'type': 'ir.actions.act_window',
            'name': f'LGAs in {self.name}',
            'view_mode': 'tree,form,kanban',
            'res_model': 'nigeria.lga',
            'domain': [('state_id', '=', self.id)],
            'context': {'default_state_id': self.id},
        }
