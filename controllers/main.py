from odoo import http
from odoo.http import request

class MyController(http.Controller):

    @http.route('/my_module/hello', type='http', auth='public',website=True )
    def hello_world(self, **kwargs):
        property_ids=request.env['estate.property'].sudo().search([])
        print(property_ids)
        return request.render("my_module.greet_template",{"property_ids":property_ids})
