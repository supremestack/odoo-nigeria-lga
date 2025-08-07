# -*- coding: utf-8 -*-
# Copyright 2025 Supreme Stack
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl).

from odoo import http
from odoo.http import request
import json


class NigeriaLGAAPI(http.Controller):
    """
    Supreme Stack Nigeria LGA API
    RESTful endpoints for external integration
    """
    
    @http.route('/api/v1/nigeria/states', 
                type='json', auth='public', methods=['GET'], 
                cors='*', csrf=False)
    def get_all_states(self, **kwargs):
        """Get all Nigerian states with their details"""
        try:
            states = request.env['nigeria.state'].sudo().search_read(
                [], 
                ['name', 'code', 'capital', 'geopolitical_zone', 'lga_count'],
                order='name asc'
            )
            return {
                'status': 'success',
                'message': 'States retrieved successfully',
                'count': len(states),
                'data': states,
                'provider': 'Supreme Stack'
            }
        except Exception as e:
            return {
                'status': 'error',
                'message': str(e),
                'provider': 'Supreme Stack'
            }
    
    @http.route('/api/v1/nigeria/states/<string:state_code>/lgas', 
                type='json', auth='public', methods=['GET'],
                cors='*', csrf=False)
    def get_state_lgas(self, state_code, **kwargs):
        """Get all LGAs for a specific state"""
        try:
            state = request.env['nigeria.state'].sudo().search([
                ('code', '=', state_code.upper())
            ], limit=1)
            
            if not state:
                return {
                    'status': 'error',
                    'message': f'State with code {state_code} not found',
                    'provider': 'Supreme Stack'
                }
            
            lgas = request.env['nigeria.lga'].sudo().search_read(
                [('state_id', '=', state.id)],
                ['name', 'code', 'headquarters', 'population'],
                order='name asc'
            )
            
            return {
                'status': 'success',
                'message': 'LGAs retrieved successfully',
                'state': state.name,
                'count': len(lgas),
                'data': lgas,
                'provider': 'Supreme Stack'
            }
        except Exception as e:
            return {
                'status': 'error',
                'message': str(e),
                'provider': 'Supreme Stack'
            }
