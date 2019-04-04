# -*- coding: utf-8 -*-
from odoo import models, fields, api
from odoo import exceptions


class MyConf(models.Model):
    _name = 'farm.app.dcollection'

    house_number = fields.Many2one('farm.app.house', string='House Number')
    ecollected = fields.Float('Trays Collected', required=True)
    date = fields.Date('Date', required=True)

    Batch = fields.Selection(
        related='house_number.batch_number', readonly=True)
    total_collected = fields.Integer(
        'Total Eggs', compute='_compute_total_eggs')
    broken = fields.Integer('Broken', required=True)
    g_eggs = fields.Integer(
        'Good', compute='_compute_good')
    stocking = fields.Many2one('farm.app.house', string='Stock Number')
    # stocking = fields.Selection(
    # related='house_number.stocking', readonly=True)

    @api.depends('ecollected')
    def _compute_total_eggs(self):
        for this in self:
            total_eggs = this.ecollected * 30
            this.total_collected = total_eggs
            if this.total_collected > 500:
                raise exceptions.Warning('exceeded')

    @api.depends('total_collected')
    def _compute_good(self):
        for this in self:
            good = this.total_collected - this.broken
            this.g_eggs = good
