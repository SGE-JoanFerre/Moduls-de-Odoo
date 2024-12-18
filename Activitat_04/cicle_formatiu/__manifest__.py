{
    'name': "Cicles Formatius Institut",
    'summary': "Gestió dels cicles formatius en un institut",
    'description': """
        Aplicació per gestionar els cicles formatius i mòduls en un institut.
    """,
    'author': "Joan Ferre",
    'website': "https://github.com/Joanfv05",
    'category': 'Custom',
    'version': '0.1',
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'security/groups.xml',
        'views/cicle_formatiu_views.xml',
        'views/modul_views.xml',
        'views/alumne_views.xml',
        'views/professor_views.xml',
    ],
    'installable': True,
    'application': True,
}
