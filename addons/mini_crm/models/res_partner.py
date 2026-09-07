from odoo import fields, models
from odoo.exceptions import UserError


class ResPartner(models.Model):
    _inherit = "res.partner"

    is_priority_customer = fields.Boolean(string="Client Prioritaire", default=False)

    def action_set_priority(self):
        for partner in self:
            if not partner.phone:
                raise UserError("Impossible de passer ce contact en prioritaire sans numéro de téléphone.")
            partner.is_priority_customer = True
