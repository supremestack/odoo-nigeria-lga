// nigeria_lga/static/src/js/nigeria_dashboard.js
/** @odoo-module **/

import { registry } from "@web/core/registry";
import { Component, useState, onWillStart, useRef, onMounted } from "@odoo/owl";
import { useService } from "@web/core/utils/hooks";

/**
 * Supreme Stack Nigeria LGA Dashboard
 * Copyright 2025 Supreme Stack
 * https://supremestack.net
 */
export class NigeriaLGADashboard extends Component {
    static template = "nigeria_lga.Dashboard";
    static props = {};
    
    setup() {
        this.rpc = useService("rpc");
        this.action = useService("action");
        this.notification = useService("notification");
        
        this.state = useState({
            // Statistics
            statesCount: 0,
            lgasCount: 0,
            statesByZone: [],
            
            // Loading states
            loading: true,
            loadingStates: false,
            loadingLgas: false,
            
            // Selected filters
            selectedZone: 'all',
            selectedState: null,
            
            // Search
            searchQuery: '',
            searchResults: [],
            
            // Charts data
            zoneChartData: [],
            populationData: [],
        });
        
        // Refs for charts
        this.chartRefs = {
            zoneChart: useRef("zoneChart"),
            populationChart: useRef("populationChart"),
        };
        
        onWillStart(async () => {
            await this.loadDashboardData();
        });
        
        onMounted(() => {
            this.initializeCharts();
        });
    }
    
    /**
     * Load initial dashboard data
     */
    async loadDashboardData() {
        try {
            this.state.loading = true;
            
            // Load statistics
            const stats = await this.rpc("/web/dataset/call_kw", {
                model: "nigeria.state",
                method: "get_dashboard_statistics",
                args: [],
                kwargs: {},
            });
            
            this.state.statesCount = stats.states_count || 37;
            this.state.lgasCount = stats.lgas_count || 774;
            this.state.statesByZone = stats.states_by_zone || this.getDefaultZoneData();
            this.state.zoneChartData = this.prepareZoneChartData(stats.states_by_zone);
            this.state.populationData = stats.population_data || [];
            
        } catch (error) {
            console.error("Error loading dashboard data:", error);
            this.notification.add("Error loading dashboard data", {
                type: "danger",
            });
            // Load default data on error
            this.loadDefaultData();
        } finally {
            this.state.loading = false;
        }
    }
    
    /**
     * Get default zone data
     */
    getDefaultZoneData() {
        return [
            { zone: 'north_central', name: 'North Central', count: 7, color: '#3498db' },
            { zone: 'north_east', name: 'North East', count: 6, color: '#9b59b6' },
            { zone: 'north_west', name: 'North West', count: 7, color: '#e74c3c' },
            { zone: 'south_east', name: 'South East', count: 5, color: '#f39c12' },
            { zone: 'south_south', name: 'South South', count: 6, color: '#2ecc71' },
            { zone: 'south_west', name: 'South West', count: 6, color: '#1abc9c' },
        ];
    }
    
    /**
     * Load default data when RPC fails
     */
    loadDefaultData() {
        this.state.statesCount = 37;
        this.state.lgasCount = 774;
        this.state.statesByZone = this.getDefaultZoneData();
    }
    
    /**
     * Prepare data for zone chart
     */
    prepareZoneChartData(zoneData) {
        if (!zoneData) return [];
        
        return zoneData.map(zone => ({
            label: zone.name,
            value: zone.count,
            color: zone.color,
            percentage: Math.round((zone.count / 37) * 100)
        }));
    }
    
    /**
     * Initialize charts using Chart.js or D3
     */
    initializeCharts() {
        // This would initialize actual charts if Chart.js is available
        // For now, we'll use CSS-based charts
        this.renderZoneChart();
        this.renderPopulationChart();
    }
    
    /**
     * Render zone distribution chart
     */
    renderZoneChart() {
        // Implement chart rendering logic
        // This is a placeholder for actual chart implementation
        console.log("Rendering zone chart with data:", this.state.zoneChartData);
    }
    
    /**
     * Render population chart
     */
    renderPopulationChart() {
        // Implement population chart rendering
        console.log("Rendering population chart");
    }
    
    /**
     * Open states list view
     */
    openStates() {
        this.action.doAction({
            type: "ir.actions.act_window",
            name: "Nigerian States",
            res_model: "nigeria.state",
            view_mode: "tree,form,kanban",
            views: [[false, "tree"], [false, "form"], [false, "kanban"]],
            target: "current",
            context: {
                search_default_active: true,
            },
        });
    }
    
    /**
     * Open LGAs list view
     */
    openLGAs() {
        this.action.doAction({
            type: "ir.actions.act_window",
            name: "Local Government Areas",
            res_model: "nigeria.lga",
            view_mode: "tree,form",
            views: [[false, "tree"], [false, "form"]],
            target: "current",
            context: {
                search_default_active: true,
            },
        });
    }
    
    /**
     * Open states filtered by zone
     */
    openZoneStates(zone) {
        this.action.doAction({
            type: "ir.actions.act_window",
            name: `States in ${zone.name}`,
            res_model: "nigeria.state",
            view_mode: "tree,form",
            domain: [["geopolitical_zone", "=", zone.zone]],
            target: "current",
        });
    }
    
    /**
     * Search for states or LGAs
     */
    async searchLocation() {
        if (!this.state.searchQuery || this.state.searchQuery.length < 2) {
            this.state.searchResults = [];
            return;
        }
        
        try {
            const results = await this.rpc("/web/dataset/call_kw", {
                model: "nigeria.state",
                method: "search_location",
                args: [this.state.searchQuery],
                kwargs: {},
            });
            
            this.state.searchResults = results;
        } catch (error) {
            console.error("Search error:", error);
        }
    }
    
    /**
     * Clear search results
     */
    clearSearch() {
        this.state.searchQuery = '';
        this.state.searchResults = [];
    }
    
    /**
     * Export data to Excel
     */
    async exportToExcel() {
        try {
            const response = await this.rpc("/nigeria/export/excel", {
                model: "nigeria.state",
                fields: ["name", "code", "capital", "geopolitical_zone", "lga_count"],
            });
            
            if (response.url) {
                window.open(response.url, "_blank");
            }
            
            this.notification.add("Export completed successfully", {
                type: "success",
            });
        } catch (error) {
            this.notification.add("Export failed", {
                type: "danger",
            });
        }
    }
    
    /**
     * Refresh dashboard data
     */
    async refreshData() {
        this.notification.add("Refreshing dashboard...", {
            type: "info",
        });
        await this.loadDashboardData();
        this.notification.add("Dashboard refreshed", {
            type: "success",
        });
    }
}
