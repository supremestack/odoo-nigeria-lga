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
    population = fields.Integer(string='Population')
    land_area = fields.Float(string='Land Area (km²)')
    
    ward_ids = fields.One2many('nigeria.ward', 'lga_id', string='Wards')
    ward_count = fields.Integer(string='Number of Wards', compute='_compute_ward_count', store=True)
    
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
    
    @api.depends('ward_ids')
    def _compute_ward_count(self):
        for lga in self:
            lga.ward_count = len(lga.ward_ids)
