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
    nigeria_ward_id = fields.Many2one('nigeria.ward', string='Ward',
                                      domain="[('lga_id', '=', nigeria_lga_id)]")
    
    @api.onchange('nigeria_state_id')
    def _onchange_nigeria_state_id(self):
        """Clear LGA and Ward when state changes"""
        if self.nigeria_state_id:
            self.nigeria_lga_id = False
            self.nigeria_ward_id = False
            if not self.country_id:
                nigeria = self.env['res.country'].search([('code', '=', 'NG')], limit=1)
                if nigeria:
                    self.country_id = nigeria.id
    
    @api.onchange('nigeria_lga_id')
    def _onchange_nigeria_lga_id(self):
        """Clear Ward when LGA changes"""
        if self.nigeria_lga_id:
            self.nigeria_ward_id = False
