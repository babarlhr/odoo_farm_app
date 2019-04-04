# -*- coding: utf-8 -*-
{
    'name': 'Farm App',
    'summary': 'learning odoo',
    'author': 'Aron langat',
    'category':'uncategorized',
    'website':'www.farm_odoo',
    "depends": [
        'base',
        'sale'
    ],
    'version':'1.0',
    'data': [
        'views/menu.xml',
        'views/record_dailyP.xml',
        'views/costing.xml',
        'views/stocking.xml',
        'views/house.xml',
        'views/res_partner.xml',

    ],
    'images': ['static/description/lo.jpeg'],
    'installable':True,
}