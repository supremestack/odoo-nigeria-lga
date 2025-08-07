# -*- coding: utf-8 -*-
# Copyright 2025 Supreme Stack
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl).

from odoo import api, fields, models, _


class NigeriaLGA(models.Model):
    """Model for Nigerian Local Government Areas"""
    _name = 'nigeria.lga'
    _description = 'Nigerian Local Government Area'
    _order = 'state_id, name'
    _rec_name = 'display_name'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    name = fields.Char(string='LGA Name', required=True, index=True, tracking=True)
    code = fields.Char(string='LGA Code', required=True, index=True)
    state_id = fields.Many2one('nigeria.state', string='State', required=True, index=True, ondelete='cascade')
    display_name = fields.Char(string='Display Name', compute='_compute_display_name', store=True)
    headquarters = fields.Char(string='Headquarters')
    
    chairman_name = fields.Char(string='Executive Chairman')
    vice_chairman_name = fields.Char(string='Vice Chairman')
    secretary_name = fields.Char(string='Secretary')
    
    population = fields.Integer(string='Population')
    land_area = fields.Float(string='Land Area (km²)')
    postal_codes = fields.Char(string='Postal Codes')
    
    phone = fields.Char(string='Phone')
    email = fields.Char(string='Email')
    website = fields.Char(string='Website')
    address = fields.Text(string='Address')
    
    active = fields.Boolean(default=True)
    
    _sql_constraints = [
        ('code_unique', 'UNIQUE(code)', 'LGA code must be unique!'),
        ('name_state_unique', 'UNIQUE(name, state_id)', 'LGA name must be unique within a state!'),
    ]
    
    @api.depends('name', 'state_id.name')
    def _compute_display_name(self):
        for lga in self:
            if lga.state_id:
                lga.display_name = f"{lga.name}, {lga.state_id.name}"
            else:
                lga.display_name = lga.name
    
    def name_get(self):
        result = []
        for lga in self:
            name = f"{lga.name} ({lga.state_id.name})" if lga.state_id else lga.name
            result.append((lga.id, name))
        return result
