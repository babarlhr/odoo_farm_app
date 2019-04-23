# -*- coding: utf-8 -*-

from odoo import fields, models, api


class ResPartner(models.Model):
    _inherit = 'res.partner'
    id_no = fields.Char('ID Number')


class ModeOfPaymnent(models.Model):
    _inherit = 'sale.order'

