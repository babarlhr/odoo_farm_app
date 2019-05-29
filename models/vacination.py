# coding: utf-8
# © 2016 Aron Langat
# License AGPL-3.0;
from odoo import models,api,fields


class Vaccination(models.Model):
    _name = 'farm.app.vaccination'

    vaccination_title = fields.Char('Vaccination Title')
    Description = fields.Char('Vaccination Description')
    house_number = fields.Selection(selection=[('House number 001', 'H001'),
                                               ('House number 002', 'H002',),
                                               ('House number 003 ', 'H003')])
    Date = fields.Date('Date')
    next_vacc_date = fields.Date('Next Vaccination Date')
    # description = fields.Char('Description')
