# -*- coding: utf-8 -*-

from odoo import api, fields, models


class ResPartner(models.Model):
    _inherit = 'res.partner'

    id_no = fields.Char('ID Number')


class ModeOfPaymnent(models.Model):
    _inherit = 'sale.order'

    mode_of_payment = fields.Selection(selection=[('mpesa', 'MPESA'),
                                                  ('cash', 'CASH'),
                                                  ('cheque', 'CHEQUE')])
    Number_of_tray = fields.Integer('Number of Trays Ordered')
    value = fields.Integer('Value',compute='_compute_sales_value')
    html = fields.Char('html')

    @api.depends('value')
    def _compute_sales_value(self):
        for this in self:
            values_of_sale = this.Number_of_tray * 290
            this.value = values_of_sale

