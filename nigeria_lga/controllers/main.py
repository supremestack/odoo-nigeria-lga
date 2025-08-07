# -*- coding: utf-8 -*-
from odoo import http
from odoo.http import request

class NigeriaLGAMain(http.Controller):
    
    @http.route('/nigeria/dashboard', type='http', auth='user')
    def dashboard(self, **kwargs):
        return request.render('nigeria_lga.dashboard_template')
