from odoo import models, fields, api, _

class UmrahService(models.Model):
    _name = "umrah.service"
    _description = "Service Master (Hotel/Transport/Catering/Activity)"
    _inherit = ["mail.thread", "mail.activity.mixin"]

    type = fields.Selection([
        ("hotel","Hotel"),
        ("intl_transport","International Transport"),
        ("local_transport","Local Transport"),
        ("transport_cycle","Local Transport Cycle"),
        ("catering","Catering"),
        ("activity","Visit/Activity"),
    ], required=True, tracking=True)
    name = fields.Char(required=True, tracking=True)
    vendor_id = fields.Many2one("res.partner", string="Vendor")
    city = fields.Char()
    room_beds = fields.Selection([("1","Single"),("2","Double"),("3","Triple"),("4","Quad")], string="Beds")
    notes = fields.Text()

class UmrahServiceContract(models.Model):
    _name = "umrah.service.contract"
    _description = "Service Contract/Rate"
    _inherit = ["mail.thread", "mail.activity.mixin"]

    name = fields.Char(default=lambda self: _("Contract"), required=True)
    service_id = fields.Many2one("umrah.service", required=True)
    service_type = fields.Selection(related="service_id.type", store=True)
    qty = fields.Float(default=1.0)
    cost_adult = fields.Float()
    cost_child = fields.Float()
    cost_infant = fields.Float()
    room_beds = fields.Selection([("1","Single"),("2","Double"),("3","Triple"),("4","Quad")])
    currency_id = fields.Many2one("res.currency", default=lambda self: self.env.company.currency_id.id)
    active = fields.Boolean(default=True)
