# -*- coding: utf-8 -*-

from odoo import fields, models


class ResPartner(models.Model):
    _inherit = 'res.partner'
    id_no = fields.Char('ID Number')


class ModeOfPaymnent(models.Model):
    _inherit = 'sale.order'
    mode_of_payment = fields.Selection(selection=[('mpesa', 'MPESA'),
                                                  ('cash', 'CASH'),
                                                  ('cheque', 'CHEQUE')])
