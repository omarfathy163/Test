from odoo import models, fields, api, _

class UmrahVisaType(models.Model):
    _name = "umrah.visa.type"
    _description = "Visa Type"

    name = fields.Char(required=True)

class UmrahVisa(models.Model):
    _name = "umrah.visa"
    _description = "Visa Request/Record"
    _inherit = ["mail.thread", "mail.activity.mixin"]

    name = fields.Char(default=lambda self: _("Visa"), required=True)
    pilgrim_id = fields.Many2one("umrah.pilgrim", required=True, ondelete="cascade")
    type_id = fields.Many2one("umrah.visa.type", required=True)
    cost = fields.Float()
    price = fields.Float()
    state = fields.Selection([
        ("new","New"),
        ("in_progress","In Progress"),
        ("requested","Requested"),
        ("issued","Issued"),
        ("rejected","Rejected"),
    ], default="new", tracking=True)
    request_ref = fields.Char(string="Request Number")
    visa_no = fields.Char(string="Visa Number")
    expiry_date = fields.Date()
    image = fields.Binary(attachment=True, string="Visa Image")
