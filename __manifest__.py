{
    'name': 'My Custom Module',
    'version': '16.0.1.0.0',
    'summary': 'A custom module for Odoo 16',
    'sequence': 10,
    'author': 'Your Name',
    'website': 'https://yourwebsite.com',
    'category': 'Custom',
    'depends': ['base','web','mail','website',],#'website_seo'
    'data': [
        'security/ir.model.access.csv',
        'views/property_view.xml',
        'views/property_tag_view.xml' ,
        'views/property_type_view.xml' ,
        'views/menu_items.xml',
        'views/property_offer_view.xml',
        'security/res_groups.xml',
        #'security/model_access.xml',
        'views/property_web_template.xml',

        'data/mail.template.xml',

        #Reports
        'report/report_template.xml',
        'report/property_report.xml',
    ],
    "assets": {
        "web.assets_backend": [
             "my_module/static/src/js/hello_client_action.js",
             "my_module/static/src/xml/hello_client_action.xml",
        ],
    },

    'installable': True,
    'application': True,
    'auto_install': False,
}
