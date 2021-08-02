# -*- coding: utf-8 -*-
{
    'name': "invoice_project",

    'summary': """
        All projects have 3 stages :
        1) Meeting Stage where a employee is assigned 
        2) Purchase Stage
        3) Handover Stage
    - When in second stage of project, Product A needs to be purchased
    - When in Handover stage, Product A is delivered to customer.""",

    'description': """
        invoice to project
    """,

    'author': "sify k Raphy",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/12.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','account','project','purchase','stock'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'demo/demo.xml',
        'views/views.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml' ,
    ],
}