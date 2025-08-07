# -*- coding: utf-8 -*-
# Copyright 2025 Supreme Stack
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl).

from odoo import api, fields, models, _


class NigeriaWard(models.Model):
    """Model for Electoral Wards within LGAs"""
    _name = 'nigeria.ward'
    _description = 'Nigerian Electoral Ward'
    _order = 'lga_id, name'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    name = fields.Char(string='Ward Name', required=True, index=True, tracking=True)
    code = fields.Char(string='Ward Code', required=True, index=True)
    lga_id = fields.Many2one('nigeria.lga', string='Local Government Area', required=True, index=True, ondelete='cascade')
    state_id = fields.Many2one('nigeria.state', string='State', related='lga_id.state_id', store=True, readonly=True)
    
    polling_units = fields.Integer(string='Number of Polling Units')
    registered_voters = fields.Integer(string='Registered Voters')
    
    councilor_name = fields.Char(string='Ward Councilor')
    
    active = fields.Boolean(default=True)
    
    _sql_constraints = [
        ('code_unique', 'UNIQUE(code)', 'Ward code must be unique!'),
        ('name_lga_unique', 'UNIQUE(name, lga_id)', 'Ward name must be unique within an LGA!'),
    ]
