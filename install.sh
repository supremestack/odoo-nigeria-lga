#!/bin/bash

#############################################
# Supreme Stack Nigeria LGA Module Installer
# Copyright 2025 Supreme Stack
#############################################

set -e

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

# Supreme Stack branding
echo -e "${GREEN}"
echo "╔════════════════════════════════════════════╗"
echo "║     SUPREME STACK NIGERIA LGA INSTALLER    ║"
echo "║         Enterprise Odoo Solutions          ║"
echo "╚════════════════════════════════════════════╝"
echo -e "${NC}"

# Check if database name is provided
if [ -z "$1" ]; then
    echo -e "${RED}Error: Database name required${NC}"
    echo "Usage: ./install.sh your_database_name"
    exit 1
fi

DATABASE=$1
ODOO_PATH="/opt/odoo"
ADDONS_PATH="${ODOO_PATH}/addons"
MODULE_NAME="nigeria_lga"

echo -e "${YELLOW}Installing Nigeria LGA module for database: ${DATABASE}${NC}"

# Install module
echo -e "${GREEN}Installing module...${NC}"
sudo -u odoo ${ODOO_PATH}/odoo-bin -d ${DATABASE} -i ${MODULE_NAME} --stop-after-init

# Restart service
echo -e "${GREEN}Restarting Odoo service...${NC}"
systemctl restart odoo

echo -e "${GREEN}"
echo "╔════════════════════════════════════════════╗"
echo "║         INSTALLATION SUCCESSFUL!           ║"
echo "╚════════════════════════════════════════════╝"
echo -e "${NC}"
echo "Module installed successfully!"
echo ""
echo "Support: support@supremestack.net"
echo "Website: https://supremestack.net"
