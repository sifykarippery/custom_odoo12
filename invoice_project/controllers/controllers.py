# -*- coding: utf-8 -*-
from odoo import http

# class InvoiceProject(http.Controller):
#     @http.route('/invoice_project/invoice_project/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/invoice_project/invoice_project/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('invoice_project.listing', {
#             'root': '/invoice_project/invoice_project',
#             'objects': http.request.env['invoice_project.invoice_project'].search([]),
#         })

#     @http.route('/invoice_project/invoice_project/objects/<model("invoice_project.invoice_project"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('invoice_project.object', {
#             'object': obj
#         })