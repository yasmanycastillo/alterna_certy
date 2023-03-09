{
    'name': "Alterna: Funcionalidades extras",
    'summary': """ Agrega ciertas funcionalidades especificas para Alterna""",
    'description': """ """,
    'author': "Yasmany Castillo",
    'website': "",
    'category': 'Category Hidden',
    'version': '13.0.0.1',
    'depends': [
        'base',
        'sale',
        'purchase',
        'account',
    ],
    'data': [
        # 'security/ir.model.access.csv',
        'security/security_groups.xml',
        'views/account_move_view.xml',
        'views/purchase_order_view.xml',
        'views/sale_order_view.xml',
    ],
    'installable': True,
}
