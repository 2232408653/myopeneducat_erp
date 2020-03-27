# -*- coding: utf-8 -*-
from odoo import http

# class OpeneducatCore(http.Controller):
#     @http.route('/openeducat_core/openeducat_core/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/openeducat_core/openeducat_core/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('openeducat_core.listing', {
#             'root': '/openeducat_core/openeducat_core',
#             'objects': http.request.env['openeducat_core.openeducat_core'].search([]),
#         })

#     @http.route('/openeducat_core/openeducat_core/objects/<model("openeducat_core.openeducat_core"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('openeducat_core.object', {
#             'object': obj
#         })