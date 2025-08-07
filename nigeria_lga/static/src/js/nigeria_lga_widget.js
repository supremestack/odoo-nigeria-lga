// ===================================================================
// nigeria_lga/static/src/js/nigeria_lga_widget.js
// ===================================================================

/** @odoo-module **/

import { registry } from "@web/core/registry";
import { standardFieldProps } from "@web/views/fields/standard_field_props";
import { Component, useState, onWillStart } from "@odoo/owl";
import { useService } from "@web/core/utils/hooks";

/**
 * Custom widget for Nigerian LGA selection
 * Provides cascading dropdowns for State -> LGA
 */
export class NigeriaLGAWidget extends Component {
    static template = "nigeria_lga.LGAWidget";
    static props = {
        ...standardFieldProps,
        stateField: { type: String, optional: true },
    };
    
    setup() {
        this.rpc = useService("rpc");
        
        this.state = useState({
            states: [],
            lgas: [],
            selectedState: null,
            selectedLGA: null,
            loading: false,
        });
        
        onWillStart(async () => {
            await this.loadStates();
            this.initializeValues();
        });
    }
    
    /**
     * Load all Nigerian states
     */
    async loadStates() {
        try {
            this.state.loading = true;
            const states = await this.rpc("/web/dataset/search_read", {
                model: "nigeria.state",
                fields: ["id", "name", "code"],
                domain: [["active", "=", true]],
                sort: "name asc",
            });
            
            this.state.states = states;
        } catch (error) {
            console.error("Error loading states:", error);
        } finally {
            this.state.loading = false;
        }
    }
    
    /**
     * Initialize selected values from record
     */
    initializeValues() {
        const record = this.props.record;
        
        if (record.data.nigeria_state_id) {
            this.state.selectedState = record.data.nigeria_state_id[0];
            this.loadLGAs(this.state.selectedState);
        }
        
        if (record.data.nigeria_lga_id) {
            this.state.selectedLGA = record.data.nigeria_lga_id[0];
        }
    }
    
    /**
     * Load LGAs for selected state
     */
    async loadLGAs(stateId) {
        if (!stateId) {
            this.state.lgas = [];
            return;
        }
        
        try {
            const lgas = await this.rpc("/web/dataset/search_read", {
                model: "nigeria.lga",
                fields: ["id", "name", "code"],
                domain: [
                    ["state_id", "=", stateId],
                    ["active", "=", true]
                ],
                sort: "name asc",
            });
            
            this.state.lgas = lgas;
        } catch (error) {
            console.error("Error loading LGAs:", error);
        }
    }
    
    /**
     * Handle state selection change
     */
    async onStateChange(ev) {
        const stateId = parseInt(ev.target.value);
        this.state.selectedState = stateId;
        this.state.selectedLGA = null;
        
        // Update record
        await this.props.record.update({
            nigeria_state_id: stateId || false,
            nigeria_lga_id: false,
        });
        
        // Load LGAs for selected state
        await this.loadLGAs(stateId);
    }
    
    /**
     * Handle LGA selection change
     */
    async onLGAChange(ev) {
        const lgaId = parseInt(ev.target.value);
        this.state.selectedLGA = lgaId;
        
        // Update record
        await this.props.record.update({
            nigeria_lga_id: lgaId || false,
        });
    }
}

// Register the widget
registry.category("fields").add("nigeria_lga_widget", NigeriaLGAWidget);
