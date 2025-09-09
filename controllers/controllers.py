# -*- coding: utf-8 -*-
# from odoo import http


# class Concejo(http.Controller):
#     @http.route('/concejo/concejo', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/concejo/concejo/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('concejo.listing', {
#             'root': '/concejo/concejo',
#             'objects': http.request.env['concejo.concejo'].search([]),
#         })

#     @http.route('/concejo/concejo/objects/<model("concejo.concejo"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('concejo.object', {
#             'object': obj
#         })

