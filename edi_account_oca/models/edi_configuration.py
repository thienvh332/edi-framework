# Copyright 2024 Camptocamp SA
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import fields, models


class EdiConfiguration(models.Model):
    _inherit = "edi.configuration"

    trigger = fields.Selection(
        selection_add=[
            ("on_send_via_email_account", "Send via Email Account"),
        ],
        ondelete={
            "on_send_via_email_account": "set default",
        },
    )
