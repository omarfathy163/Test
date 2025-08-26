from odoo import models, fields, api, _

class UmrahGroup(models.Model):
    _name = "umrah.group"
    _description = "Umrah Group"
    _inherit = ["mail.thread", "mail.activity.mixin"]

    name = fields.Char(required=True, tracking=True)
    code = fields.Char(string="Code", tracking=True)
    main_agent_id = fields.Many2one("umrah.travel.agent", string="Main Agent", tracking=True)
    sub_agent_id = fields.Many2one("umrah.travel.agent", string="Sub Agent", tracking=True, domain="[('type','=','sub')]")
    company_supervisor_id = fields.Many2one("res.users", string="Company Supervisor")
    agent_supervisor_id = fields.Many2one("umrah.agent.employee", string="Agent Supervisor")
    state = fields.Selection([
        ("with_agent","With Agent"),
        ("new","New"),
        ("visa_processing","Visa Processing"),
        ("done","Completed"),
    ], default="with_agent", tracking=True)

    program_line_ids = fields.One2many("umrah.group.program.line","group_id", string="Program Lines")
    pilgrim_ids = fields.One2many("umrah.pilgrim","group_id", string="Pilgrims")

    invoice_count = fields.Integer(compute="_compute_invoice_count")

    def _compute_invoice_count(self):
        for rec in self:
            rec.invoice_count = self.env["account.move"].search_count([("invoice_origin","=", rec.name)])

    def action_view_invoices(self):
        self.ensure_one()
        action = self.env.ref("account.action_move_out_invoice_type").read()[0]
        action["domain"] = [("invoice_origin","=", self.name)]
        return action

class UmrahGroupProgramLine(models.Model):
    _name = "umrah.group.program.line"
    _description = "Group Program Line"

    group_id = fields.Many2one("umrah.group", required=True, ondelete="cascade")
    service_type = fields.Selection([
        ("hotel","Hotel"),
        ("intl_transport","International Transport"),
        ("local_transport","Local Transport"),
        ("catering","Catering"),
        ("activity","Visit/Activity"),
    ], required=True)
    service_id = fields.Many2one("umrah.service", domain="[('type','=',service_type)]")
    city = fields.Char()
    room_beds = fields.Selection([("1","Single"),("2","Double"),("3","Triple"),("4","Quad")])
    checkin = fields.Datetime()
    checkout = fields.Datetime()
    duration_days = fields.Integer(compute="_compute_duration", store=False)
    carrier_name = fields.Char(string="Carrier/Company")
    go_date = fields.Datetime(string="Departure")
    return_date = fields.Datetime(string="Return")
    qty = fields.Float(default=1.0)
    cost = fields.Float()
    price = fields.Float()

    def _compute_duration(self):
        for rec in self:
            rec.duration_days = 0
            if rec.checkin and rec.checkout:
                delta = fields.Datetime.to_datetime(rec.checkout) - fields.Datetime.to_datetime(rec.checkin)
                rec.duration_days = max(int(delta.total_seconds() // 86400), 0)
