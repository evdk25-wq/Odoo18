from odoo import fields, models


class Opportunity(models.Model):
    _name = "mini.crm.opportunity"
    _description = "Commercial Opportunity"

    name = fields.Char(string="Opportunity", required=True)
    partner_id = fields.Many2one(
        "res.partner",
        string="Customer",
    )
    expected_revenue = fields.Float(
        string="Expected Revenue",
    )
    stage = fields.Selection(
        [
            ("new", "New"),
            ("negotiation", "Negotiation"),
            ("won", "Won"),
            ("lost", "Lost"),
        ],
        string="Stage",
        default="new",
    )
    notes = fields.Text(string="Notes")
