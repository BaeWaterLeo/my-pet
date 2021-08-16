# -*- coding: utf-8 -*-
{
    'name': "My pet",
    'summary': """My pet model""",
    'description': """Managing pet information""",
    'author': "bae_water_leo",
    'website': "https://mypet.info",
    'category': 'Uncategorized',
    'version': '0.1',
    'depends': [
        'product',
    ],
    'data': [
        'security/ir.model.access.csv',
        'views/my_pet_views.xml',
    ],
    'installable': True,
    'application': True,
}