from odoo import models, fields, api, _

class UmrahTravelAgent(models.Model):
    _name = "umrah.travel.agent"
    _description = "Travel Agent"

    name = fields.Char(required=True)
    license_no = fields.Char(string="License Number")
    cr_no = fields.Char(string="Commercial Registration")
    country_id = fields.Many2one("res.country", string="Country")
    state_id = fields.Many2one("res.country.state", string="State")
    street = fields.Char()
    city = fields.Char()
    phone = fields.Char()
    email = fields.Char()
    website = fields.Char()
    partner_id = fields.Many2one("res.partner", string="Partner", ondelete="set null")
    type = fields.Selection([("main","Main"),("sub","Sub")], default="main", required=True)
    parent_agent_id = fields.Many2one("umrah.travel.agent", string="Main Agent")
    branch_ids = fields.One2many("umrah.travel.agent","parent_agent_id", string="Branches")
    employee_ids = fields.One2many("umrah.agent.employee","agent_id", string="Employees")

    _sql_constraints = [
        ("name_uniq","unique(name)","Agent name must be unique."),
    ]

class UmrahAgentEmployee(models.Model):
    _name = "umrah.agent.employee"
    _description = "Agent Employee"

    name = fields.Char(required=True)
    email = fields.Char()
    mobile = fields.Char()
    permission = fields.Selection([("read","Read Only"),("edit","Add & Edit")], default="read", required=True)
    agent_id = fields.Many2one("umrah.travel.agent", required=True, ondelete="cascade")
    user_id = fields.Many2one("res.users", string="Portal User", help="Link to a portal/internal user.")
    active = fields.Boolean(default=True)
