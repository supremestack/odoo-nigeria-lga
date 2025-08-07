// ===================================================================
// nigeria_lga/static/src/js/utils.js
// ===================================================================

/** @odoo-module **/

/**
 * Utility functions for Nigeria LGA module
 * Copyright 2025 Supreme Stack
 */

/**
 * Format number with thousand separators
 */
export function formatNumber(num) {
    if (!num) return '0';
    return num.toString().replace(/\B(?=(\d{3})+(?!\d))/g, ",");
}

/**
 * Get geopolitical zone display name
 */
export function getZoneDisplayName(zone) {
    const zones = {
        'north_central': 'North Central',
        'north_east': 'North East',
        'north_west': 'North West',
        'south_east': 'South East',
        'south_south': 'South South',
        'south_west': 'South West',
    };
    return zones[zone] || zone;
}

/**
 * Get zone color
 */
export function getZoneColor(zone) {
    const colors = {
        'north_central': '#3498db',
        'north_east': '#9b59b6',
        'north_west': '#e74c3c',
        'south_east': '#f39c12',
        'south_south': '#2ecc71',
        'south_west': '#1abc9c',
    };
    return colors[zone] || '#95a5a6';
}

/**
 * Nigerian states data
 */
export const NIGERIAN_STATES = {
    'FCT': { name: 'Federal Capital Territory', zone: 'north_central', lgas: 6 },
    'ABI': { name: 'Abia', zone: 'south_east', lgas: 17 },
    'ADA': { name: 'Adamawa', zone: 'north_east', lgas: 21 },
    'AKW': { name: 'Akwa Ibom', zone: 'south_south', lgas: 31 },
    'ANA': { name: 'Anambra', zone: 'south_east', lgas: 21 },
    'BAU': { name: 'Bauchi', zone: 'north_east', lgas: 20 },
    'BAY': { name: 'Bayelsa', zone: 'south_south', lgas: 8 },
    'BEN': { name: 'Benue', zone: 'north_central', lgas: 23 },
    'BOR': { name: 'Borno', zone: 'north_east', lgas: 27 },
    'CRO': { name: 'Cross River', zone: 'south_south', lgas: 18 },
    'DEL': { name: 'Delta', zone: 'south_south', lgas: 25 },
    'EBO': { name: 'Ebonyi', zone: 'south_east', lgas: 13 },
    'EDO': { name: 'Edo', zone: 'south_south', lgas: 18 },
    'EKI': { name: 'Ekiti', zone: 'south_west', lgas: 16 },
    'ENU': { name: 'Enugu', zone: 'south_east', lgas: 17 },
    'GOM': { name: 'Gombe', zone: 'north_east', lgas: 11 },
    'IMO': { name: 'Imo', zone: 'south_east', lgas: 27 },
    'JIG': { name: 'Jigawa', zone: 'north_west', lgas: 27 },
    'KAD': { name: 'Kaduna', zone: 'north_west', lgas: 23 },
    'KAN': { name: 'Kano', zone: 'north_west', lgas: 44 },
    'KAT': { name: 'Katsina', zone: 'north_west', lgas: 34 },
    'KEB': { name: 'Kebbi', zone: 'north_west', lgas: 21 },
    'KOG': { name: 'Kogi', zone: 'north_central', lgas: 21 },
    'KWA': { name: 'Kwara', zone: 'north_central', lgas: 16 },
    'LAG': { name: 'Lagos', zone: 'south_west', lgas: 20 },
    'NAS': { name: 'Nasarawa', zone: 'north_central', lgas: 13 },
    'NIG': { name: 'Niger', zone: 'north_central', lgas: 25 },
    'OGU': { name: 'Ogun', zone: 'south_west', lgas: 20 },
    'OND': { name: 'Ondo', zone: 'south_west', lgas: 18 },
    'OSU': { name: 'Osun', zone: 'south_west', lgas: 30 },
    'OYO': { name: 'Oyo', zone: 'south_west', lgas: 33 },
    'PLA': { name: 'Plateau', zone: 'north_central', lgas: 17 },
    'RIV': { name: 'Rivers', zone: 'south_south', lgas: 23 },
    'SOK': { name: 'Sokoto', zone: 'north_west', lgas: 23 },
    'TAR': { name: 'Taraba', zone: 'north_east', lgas: 16 },
    'YOB': { name: 'Yobe', zone: 'north_east', lgas: 17 },
    'ZAM': { name: 'Zamfara', zone: 'north_west', lgas: 14 },
};

/**
 * Export functions
 */
export default {
    formatNumber,
    getZoneDisplayName,
    getZoneColor,
    NIGERIAN_STATES,
};
