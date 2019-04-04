# -*- coding: utf-8 -*-
from odoo import models, fields, api


class Costing(models.Model):
    _name = 'farm.app.costing'
    feeds_type = fields.Selection(selection=[('Type1', 'Chick mash',),
                                       ('Type2', 'Protein'),
                                       ('Type3', 'Multivitamin')], required=True)

    amount = fields.Integer('Feeds Amount', required=True)
    date = fields.Date('Date')
    purchase_price = fields.Integer('Purchasing Price',compute='_compute_costoffeeds')

    @api.depends('amount')
    def _compute_costoffeeds(self):
        for this in self:
            cost_of_feeds = this.amount * 500
            this.purchase_price = cost_of_feeds

