# -*- coding: utf-8 -*-
{
    'name': "concejo",

    'summary': "Concejo DMS Patch",

    'description': """
    """,

    'author': "Romualdo Jr",
    'website': "https://github.com/coderomz/concejo",

    'license': 'AGLP',
    'version': '18.0.1.0.0',

    'category': 'Website',

    # any module necessary for this one to work correctly
    'depends': ['website_slides'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/advance_search_templates.xml',
        'views/courses_all_bodyclass.xml',
        'views/res_users.xml'
    ],

    'assets': {
        'web.assets_frontend': [
            'concejo/static/src/scss/concejo_style_frontend.scss',
        ]
    },

    "installable": True,
    "application": True,

}

