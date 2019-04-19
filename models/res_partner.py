# -*- coding: utf-8 -*-

from odoo import fields, models, api


class ResPartner(models.Model):
    _inherit = 'res.partner'
    id_no = fields.Char('ID Number')


class ModeOfPaymnent(models.Model):
    _inherit = 'sale.order'
    mode_of_payment = fields.Selection(selection=[('mpesa', 'MPESA'),
                                                  ('cash', 'CASH'),
                                                  ('cheque', 'CHEQUE')])
    eggs_sold = fields.Integer('Eggs Sold')
    amount_totall = fields.Integer('Amount Paid', compute='_compute_amount')

    @api.depends('eggs_sold')
    def _compute_amount(self):
        for this in self:
            total_sales = this.eggs_sold * 10
            this.amount_totall = total_sales
