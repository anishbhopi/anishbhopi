# -*- coding: utf-8 -*-
{
    'name': "collegepce",

    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",

    'description': """
        Long description of module's purpose
    """,

    'author': " Anish",
    'website': "http://www.yourcompany.com", 'category': 'EDU1',
    'version': '1',


    'depends': ['base'],


    'data': ['/home/anish/Documents/bista/odoo/custom_addons/collegepce/views/college_student_viewz.xml',
             '/home/anish/Documents/bista/odoo/custom_addons/collegepce/views/college_course_view.xml',
             '/home/anish/Documents/bista/odoo/custom_addons/collegepce/views/college_staff_view.xml',
             '/home/anish/Documents/bista/odoo/custom_addons/collegepce/security/ir.model.access.csv'],



    'installable': True,
    'application': True,
    'auto_install': False,
    'post_init_hook': '_account_post_init',
}


