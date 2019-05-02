# coding: utf-8
# © 2016 Aron Langat
# License AGPL-3.0;
from odoo import models
from odoo import modules


graph = modules.graph.Graph()


class Dashboard(models.Model):
    _name = 'student.portal.dashboard'
