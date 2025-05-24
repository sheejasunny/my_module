from xlsxwriter.contenttypes import defaults

from odoo import models, fields, api
import logging
from odoo.exceptions import ValidationError



class Property(models.Model):
    _name = 'estate.property'
    #_inherit = ['mail.thread', ]
    #_inherit = ['utm.mixin', 'website.seo.metadata']
    _description = 'Estate Property'

    name = fields.Char(string="Name",require=True,tracking=True)
    tag_ids =  fields.Many2many('estate.property.tag',string="Property Tag")
    type_ids = fields.Many2one('estate.property.type', string="Property Type")
    description = fields.Text(string="Description")
    postcode = fields.Char(string="Postcode")
    date_availability = fields.Date(string="Available From")
    expected_price = fields.Float(string="Expected Price")
    best_offer = fields.Float(string="Best Offer")
    selling_price = fields.Float(string="Selling Price")
    bed_rooms = fields.Float(string="Bed Rooms")
    living_area = fields.Integer(string="Living Area")
    facades = fields.Integer(string="Facades")
    garage = fields.Boolean(string="Garage",default=False)
    garden = fields.Boolean(string="Garden", default=False)
    garden_area = fields.Integer(string="Garden Area")
    garden_orientation = fields.Selection([('north','North'),('south','South'),('east','East'),('west','West')],string='Garden Orientation',default='north')
    offer_ids = fields.One2many('estate.property.offer','property_id',string="Offers",tracking=True)
    sales_id = fields.Many2one('res.users', string="Salesman")
    buyer_id = fields.Many2one('res.partner',string="Buyer",)
    phone =  fields.Char(string='phone',related='buyer_id.phone' ,tracking=True)
    state = fields.Selection([('new','New'),
                              ('received','Offer Received'),
                              ('accepted','Offer Accepted'),
                              ('sold','Sold'),
                              ('cancel','Cancel'),],
                              default='new',string='Status', tracking=True)
    '''website_url = fields.Char('Website URL', compute='_compute_website_url')
    is_published = fields.Boolean(string='Published on Website', default=False)

    def _compute_website_url(self):
        for record in self:
            record.website_url = f"/properties/{record.id}"'''

    @api.depends('living_area', 'garden_area')
    def _compute_total_area(self):
        for rec in self:
            rec.total_area = rec.living_area + rec.garden_area
    total_area = fields.Integer(string="Total Area" ,compute=_compute_total_area)

    '''def _get_alias_model_name(self):
        return 'estate.property' '''

    def action_send_email(self):
        mail_template = self.env.ref('my_module.email_template_offfer')
        mail_template.send_mail(self.id, force_send=True)

    def action_sold(self):
        for record in self:
            record.state = 'sold'
    def action_cancel(self):
            self.state = 'cancel'
    # SERVER ACTION
    def extend_best_offer(self):
        for record in self:
            if record.expected_price:
                increase = record.expected_price * 0.10
                record.best_offer += increase

    def extend_scheduled_task_offer(self):
        offer_ids=self.env['estate.property'].search([])
        for offer in offer_ids:
            offer.best_offer=offer.best_offer - 5

    def action_url_action(self):
        return {
            'type': 'ir.actions.act_url',
            'url': 'https://www.vidyaacademy.ac.in/',
            'target': 'new',  # open in new tab
        }

    def _get_report_base_filename(self):
        self.ensure_one()
        return 'Estate Property - %s' % self.name
    def _get_emails(self):
        return ','.join(self.offer_ids.mapped('partner_email'))

class PropertyType(models.Model):
    _name = 'estate.property.type'
    _description = 'Property Type'

    name = fields.Char(string="Name", )


class PropertyTag(models.Model):
    _name = 'estate.property.tag'
    _description = 'Property Tag'

    name = fields.Char(string="Name",)
    color=fields.Integer(string="Color",)

