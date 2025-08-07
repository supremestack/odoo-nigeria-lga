// ===================================================================
// nigeria_lga/static/src/js/nigeria_map_view.js
// ===================================================================

/** @odoo-module **/

import { registry } from "@web/core/registry";
import { Component, useState, onMounted, useRef } from "@odoo/owl";
import { useService } from "@web/core/utils/hooks";

/**
 * Map view for Nigerian states and LGAs
 * Visual representation of geographical data
 */
export class NigeriaMapView extends Component {
    static template = "nigeria_lga.MapView";
    static props = {
        resModel: String,
        domain: { type: Array, optional: true },
    };
    
    setup() {
        this.rpc = useService("rpc");
        this.mapContainer = useRef("mapContainer");
        
        this.state = useState({
            selectedZone: null,
            selectedState: null,
            hoveredState: null,
            stateData: [],
            loading: true,
        });
        
        onMounted(() => {
            this.initializeMap();
        });
    }
    
    /**
     * Initialize the map
     */
    async initializeMap() {
        try {
            // Load state data
            await this.loadStateData();
            
            // Render SVG map or canvas map
            this.renderMap();
            
            // Add event listeners
            this.attachEventListeners();
            
        } catch (error) {
            console.error("Error initializing map:", error);
        } finally {
            this.state.loading = false;
        }
    }
    
    /**
     * Load state geographical data
     */
    async loadStateData() {
        const data = await this.rpc("/web/dataset/search_read", {
            model: "nigeria.state",
            fields: ["id", "name", "code", "geopolitical_zone", "lga_count", "population"],
            domain: this.props.domain || [],
        });
        
        this.state.stateData = data;
    }
    
    /**
     * Render the map using SVG or Canvas
     */
    renderMap() {
        // This is a simplified version
        // In production, you would use actual geographical data
        const container = this.mapContainer.el;
        
        // Create SVG element
        const svg = document.createElementNS("http://www.w3.org/2000/svg", "svg");
        svg.setAttribute("width", "100%");
        svg.setAttribute("height", "500");
        svg.setAttribute("viewBox", "0 0 800 600");
        
        // Add states as rectangles (simplified)
        this.state.stateData.forEach((state, index) => {
            const rect = this.createStateElement(state, index);
            svg.appendChild(rect);
        });
        
        container.appendChild(svg);
    }
    
    /**
     * Create visual element for a state
     */
    createStateElement(state, index) {
        const rect = document.createElementNS("http://www.w3.org/2000/svg", "rect");
        
        // Calculate position (simplified grid layout)
        const x = (index % 6) * 130 + 10;
        const y = Math.floor(index / 6) * 80 + 10;
        
        rect.setAttribute("x", x);
        rect.setAttribute("y", y);
        rect.setAttribute("width", "120");
        rect.setAttribute("height", "70");
        rect.setAttribute("fill", this.getZoneColor(state.geopolitical_zone));
        rect.setAttribute("stroke", "#fff");
        rect.setAttribute("stroke-width", "2");
        rect.setAttribute("data-state-id", state.id);
        rect.setAttribute("class", "state-element");
        rect.style.cursor = "pointer";
        
        // Add text label
        const text = document.createElementNS("http://www.w3.org/2000/svg", "text");
        text.setAttribute("x", x + 60);
        text.setAttribute("y", y + 35);
        text.setAttribute("text-anchor", "middle");
        text.setAttribute("fill", "#fff");
        text.setAttribute("font-size", "12");
        text.textContent = state.code;
        
        return rect;
    }
    
    /**
     * Get color for geopolitical zone
     */
    getZoneColor(zone) {
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
     * Attach event listeners to map elements
     */
    attachEventListeners() {
        const elements = this.mapContainer.el.querySelectorAll('.state-element');
        
        elements.forEach(element => {
            element.addEventListener('click', (e) => this.onStateClick(e));
            element.addEventListener('mouseenter', (e) => this.onStateHover(e));
            element.addEventListener('mouseleave', (e) => this.onStateLeave(e));
        });
    }
    
    /**
     * Handle state click
     */
    onStateClick(event) {
        const stateId = parseInt(event.target.dataset.stateId);
        const state = this.state.stateData.find(s => s.id === stateId);
        
        if (state) {
            this.openStateDetails(state);
        }
    }
    
    /**
     * Handle state hover
     */
    onStateHover(event) {
        const stateId = parseInt(event.target.dataset.stateId);
        this.state.hoveredState = stateId;
        
        // Show tooltip
        this.showTooltip(event, stateId);
    }
    
    /**
     * Handle state leave
     */
    onStateLeave(event) {
        this.state.hoveredState = null;
        this.hideTooltip();
    }
    
    /**
     * Show tooltip with state information
     */
    showTooltip(event, stateId) {
        const state = this.state.stateData.find(s => s.id === stateId);
        if (!state) return;
        
        // Create or update tooltip
        let tooltip = document.getElementById('map-tooltip');
        if (!tooltip) {
            tooltip = document.createElement('div');
            tooltip.id = 'map-tooltip';
            tooltip.className = 'map-tooltip';
            document.body.appendChild(tooltip);
        }
        
        tooltip.innerHTML = `
            <strong>${state.name}</strong><br>
            Zone: ${state.geopolitical_zone.replace('_', ' ').toUpperCase()}<br>
            LGAs: ${state.lga_count}<br>
            Population: ${(state.population || 0).toLocaleString()}
        `;
        
        tooltip.style.display = 'block';
        tooltip.style.left = event.pageX + 10 + 'px';
        tooltip.style.top = event.pageY + 10 + 'px';
    }
    
    /**
     * Hide tooltip
     */
    hideTooltip() {
        const tooltip = document.getElementById('map-tooltip');
        if (tooltip) {
            tooltip.style.display = 'none';
        }
    }
    
    /**
     * Open state details
     */
    openStateDetails(state) {
        this.env.services.action.doAction({
            type: "ir.actions.act_window",
            res_model: "nigeria.state",
            res_id: state.id,
            views: [[false, "form"]],
            target: "current",
        });
    }
}

// Register the map view
registry.category("views").add("nigeria_map", NigeriaMapView);
