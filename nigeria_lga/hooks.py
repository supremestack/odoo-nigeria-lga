# nigeria_lga/hooks.py
# -*- coding: utf-8 -*-
# Copyright 2025 Supreme Stack
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl).

from odoo import api, SUPERUSER_ID
import logging

_logger = logging.getLogger(__name__)

# Import the complete data
from .data.nigeria_complete_data import NIGERIA_STATES_DATA


def post_init_hook(cr, registry):
    """
    Post-installation hook to load all Nigerian states and LGAs data
    """
    _logger.info('Starting Nigeria LGA data initialization by Supreme Stack...')
    
    env = api.Environment(cr, SUPERUSER_ID, {})
    
    # Ensure Nigeria country exists
    nigeria = env['res.country'].search([('code', '=', 'NG')], limit=1)
    if not nigeria:
        nigeria = env['res.country'].create({
            'name': 'Nigeria',
            'code': 'NG',
            'phone_code': 234,
        })
    
    # Load all states and LGAs
    load_complete_data(env, nigeria)
    
    _logger.info('Successfully loaded all Nigerian states and LGAs')


def load_complete_data(env, nigeria):
    """
    Load all Nigerian states and LGAs from the complete data file
    """
    states_created = 0
    lgas_created = 0
    
    for state_code, state_data in NIGERIA_STATES_DATA.items():
        # Check if state already exists
        existing_state = env['nigeria.state'].search([
            ('code', '=', state_code)
        ], limit=1)
        
        if not existing_state:
            # Create state
            _logger.info(f"Creating state: {state_data['name']}")
            
            state = env['nigeria.state'].create({
                'name': state_data['name'],
                'code': state_code,
                'capital': state_data['capital'],
                'geopolitical_zone': state_data['zone'],
            })
            states_created += 1
            
            # Create LGAs for this state
            for lga_name in state_data['lgas']:
                lga_code = f"{state_code}_{lga_name.replace(' ', '_').replace('/', '_').upper()}"
                
                env['nigeria.lga'].create({
                    'name': lga_name,
                    'code': lga_code,
                    'state_id': state.id,
                    'headquarters': lga_name,  # Default headquarters to LGA name
                })
                lgas_created += 1
        else:
            _logger.info(f"State {state_data['name']} already exists, checking LGAs...")
            
            # Check and create missing LGAs
            for lga_name in state_data['lgas']:
                existing_lga = env['nigeria.lga'].search([
                    ('name', '=', lga_name),
                    ('state_id', '=', existing_state.id)
                ], limit=1)
                
                if not existing_lga:
                    lga_code = f"{state_code}_{lga_name.replace(' ', '_').replace('/', '_').upper()}"
                    
                    env['nigeria.lga'].create({
                        'name': lga_name,
                        'code': lga_code,
                        'state_id': existing_state.id,
                        'headquarters': lga_name,
                    })
                    lgas_created += 1
    
    _logger.info(f"Data loading complete: {states_created} states and {lgas_created} LGAs created")
    
    # Verify counts
    total_states = env['nigeria.state'].search_count([])
    total_lgas = env['nigeria.lga'].search_count([])
    
    _logger.info(f"Total in database: {total_states} states, {total_lgas} LGAs")
    
    # Log statistics by zone
    for zone in ['north_central', 'north_east', 'north_west', 'south_east', 'south_south', 'south_west']:
        zone_states = env['nigeria.state'].search_count([('geopolitical_zone', '=', zone)])
        _logger.info(f"Zone {zone}: {zone_states} states")


def uninstall_hook(cr, registry):
    """
    Uninstall hook for cleanup
    """
    _logger.info('Uninstalling Nigeria LGA module')
    # Add any cleanup logic if needed
    pass
