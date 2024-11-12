# Copyright 2024 Camptocamp SA
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).


from odoo import fields, models


class ResPartner(models.Model):
    _inherit = "res.partner"

    edi_account_conf_ids = fields.Many2many(
        string="EDI Account Config Ids",
        comodel_name="edi.configuration",
        relation="res_partner_edi_configuration_account_rel",
        column1="partner_id",
        column2="conf_id",
        domain="[('model_name', '=', 'account.move')]",
    )
