# -*- coding: utf-8 -*-
{
    'name' : 'First Module',
    'version' : '0.1',
    'summary': 'First Module',
    'author': 'LerokLerok',
    'company': "LerokInc",
    'sequence': 5,
    'description': """ ###First Module###  """,
    'category': 'Tools',
    'website': 'https://www.lera.com',
    'depends' : ['base', 'contacts', 'hr', 'account'],
    'data': [
        'security/ir.model.access.csv',
        'wizard/wizard_task_modal.xml',
        'views/first_module.xml',
        'views/wizard_task.xml'


    ],
    'demo': [
    ],
    'images': ['static/description/icon.png'],
    'installable': True,
    'application': True,
    'auto_install': False


}
