# -*- coding: utf-8 -*-
{
    'name': "College_Mgmt",


    'summary': """
        college management """,

    'description': " College Management Inclueds  1)Student 2)Teacher Mgmt 3)Administration Mgmt 4)billing ",

    'author': "Anish",
    #'website': "www.strkers.ml",
    #'image': ['odoo/custom_addons/collegeMgmt/static/src/img/icon.png'],


    'category': 'EDU',
    'version': '1',


    'depends': ['base'],


    'data': ['/home/anish/Documents/bista/odoo/custom_addons/collegeMgmt/views/student_views.xml',
            'odoo/custom_addons/collegeMgmt/security/ir.model.access.csv'],

    #'demo':[],
    'installable':True,
    'application':True,

}
