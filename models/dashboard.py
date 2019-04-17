# coding: utf-8
# © 2016 Aron Langat
# License AGPL-3.0;
from odoo import models,api,fields
from odoo import modules


graph = modules.graph.Graph()


class Dashboard(models.Model):
    _name = 'farm.app.dashboard'

