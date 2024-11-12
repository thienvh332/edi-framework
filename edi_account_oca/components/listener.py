# Copyright 2024 Camptocamp SA
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo.addons.component.core import Component


class EDIConfigAccountListener(Component):
    _name = "edi.listener.config.account.move"
    _inherit = "base.event.listener"
    _apply_on = ["account.move"]

    def on_send_via_email_account(self, record):
        trigger = "on_send_via_email_account"
        confs = record.partner_id.edi_account_conf_ids.edi_get_conf(trigger)
        for conf in confs:
            conf.edi_exec_snippet_do(record)
