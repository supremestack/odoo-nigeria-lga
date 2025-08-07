# -*- coding: utf-8 -*-
# Copyright 2025 Supreme Stack
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl).

from odoo import api, fields, models


class ResPartner(models.Model):
    """Extend res.partner to include Nigerian LGA fields"""
    _inherit = 'res.partner'

    nigeria_state_id = fields.Many2one('nigeria.state', string='Nigerian State')
    nigeria_lga_id = fields.Many2one('nigeria.lga', string='Local Government Area', 
                                     domain="[('state_id', '=', nigeria_state_id)]")
    
    @api.onchange('nigeria_state_id')
    def _onchange_nigeria_state_id(self):
        """Clear LGA when state changes"""
        if self.nigeria_state_id:
            self.nigeria_lga_id = False
            if not self.country_id:
                nigeria = self.env['res.country'].search([('code', '=', 'NG')], limit=1)
                if nigeria:
                    self.country_id = nigeria.id
    
    @api.onchange('country_id')
    def _onchange_country_id(self):
        """Clear Nigerian fields if country is not Nigeria"""
        if self.country_id and self.country_id.code != 'NG':
            self.nigeria_state_id = False
            self.nigeria_lga_id = False
