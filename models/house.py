# coding: utf-8
# © 2016 Aron Langat
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
from odoo import models, fields


class House(models.Model):
    _name = 'farm.app.house'
    _rec_name = 'house_number'

    house_number = fields.Selection(
        selection=[('House number 001', 'H001'),
                   ('House number 002', 'H002',),
                   ('House number 003 ', 'H003')])
    batch_number = fields.Selection(selection=[
        ('Batch01', 'B001'), ('Batch02', 'B002')])
    stock_number = fields.Float('Number of hens')
