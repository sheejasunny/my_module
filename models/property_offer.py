from datetime import timedelta

from odoo import models, fields, api
from odoo.exceptions import ValidationError
from datetime import datetime


def _(param): # for remove _ raise condition error not included in online course
    pass


#Abstract Transient ,Regular  Model
class AbstractOffer(models.AbstractModel):
    _name = 'abstract.model.offer'
    _description = ' Abstract Property Offer'

    partner_email = fields.Char(string='Email')
    partner_phone = fields.Char(string='Phone')


class PropertyOffer(models.Model):
    _name = 'estate.property.offer'
    _inherit = ['abstract.model.offer']
    _description = 'Estate Property Offer'

    @api.model
    def _set_create_date(self):
        return fields.Date.today()

    name = fields.Char(string="Description")
    price = fields.Float(string="Price")
    status = fields.Selection([('draft','Draft'),('accepted','Accepted'),('refused', 'Refused')],string='Status')
    partner_id = fields.Many2one('res.partner', string='Customer')
    partner_email = fields.Char(string='Customer Email',related='partner_id.email')
    property_id = fields.Many2one('estate.property', string='Property')
    validity = fields.Integer(string='validity')
    deadline = fields.Date(string='Deadline' ,compute='_compute_deadline', )
    create_date = fields.Date(string='Create Date' ,default=_set_create_date)

    @api.depends('create_date', 'validity')
    def _compute_deadline(self):
        for rec in self:
            if rec.create_date and rec.validity:
                rec.deadline = rec.create_date + timedelta(days=rec.validity)

                # Perform validation here directly
                if rec.deadline <= rec.create_date:
                    raise ValidationError(_("Deadline cannot be before creation date"))
            else:
                rec.deadline = False

    @api.model_create_multi
    def create (self,vals):
        for rec in self:
            if not rec.get('create_date'):
                rec['create_date'] = fields.Date.today()
        return super(PropertyOffer,self).create(vals)

    def write (self,vals):
        for rec in self:
            if not rec.get('create_date'):
                rec['create_date'] = fields.Date.today()
        return super(PropertyOffer,self).write(vals)

    def action_accept(self):
        for offer in self:
            offer.status = 'accepted'

    def action_refuse(self):
        for offer in self:
            offer.status = 'refused'








