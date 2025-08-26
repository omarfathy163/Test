from odoo import models, fields, api, _

class UmrahPilgrim(models.Model):
    _name = "umrah.pilgrim"
    _description = "Pilgrim/Beneficiary"
    _inherit = ["mail.thread", "mail.activity.mixin"]

    name = fields.Char(required=True, tracking=True)
    passport_no = fields.Char(required=True, tracking=True)
    birth_date = fields.Date()
    passport_issue_date = fields.Date()
    passport_expiry_date = fields.Date()
    phone = fields.Char()
    status = fields.Selection([
        ("new","New"),
        ("processing","Processing"),
        ("visa_issued","Visa Issued"),
        ("delivered","Delivered"),
    ], default="new", tracking=True)
    passport_image = fields.Binary(attachment=True)
    photo = fields.Binary(attachment=True)
    other_docs = fields.Binary(attachment=True)
    visa_request_no = fields.Char()
    visa_no = fields.Char()
    visa_valid_until = fields.Date()
    presence_state = fields.Selection([("arrived","Arrived"),("departed","Departed")])
    group_id = fields.Many2one("umrah.group", string="Group")

    _sql_constraints = [
        ("passport_unique", "unique(passport_no)", "Passport No must be unique."),
    ]
