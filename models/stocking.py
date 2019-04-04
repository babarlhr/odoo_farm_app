# coding: utf-8
# © 2016 Aron Langat
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import api, fields, models


class Stocking(models.Model):
    _name = 'farm.app.stocking'
    _rec_name = 'stocking'

    house_number = fields.Many2one('farm.app.house', string='House Number')
    batch_number = fields.Selection(related='house_number.batch_number')
    date = fields.Date('DATE', required=True)
    stocking = fields.Integer('Stock')
