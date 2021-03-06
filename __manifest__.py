# -*- coding: utf-8 -*-
{
    'name': "Libros",

    'summary': """
        Modulo para la gestion de libros de una biblioteca""",

    'description': """
        Modulo que permite añadir, modificar y eliminar libros
    """,

    'author': "ComicSans",
    'website': "",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/10.0/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base' , 'report'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
        'views/view_grupo.xml',
        'views/views_alumnos.xml',
        'views/views_libros.xml',
        'security/security.xml',
        'security/ir.model.access.csv',
        'report/libro_report.xml'
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
        
    ],
}
