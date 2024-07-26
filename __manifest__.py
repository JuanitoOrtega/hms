{
    "name": "Hospital Management System",
    "author": "Creativa.dev",
    "license": "LGPL-3",
    "version": "17.0.1.1",
    "category": "Healthcare",
    "summary": 'Gestión de pacientes y citas para hospitales',
    'description': 'Este módulo gestiona pacientes y citas para hospitales.',
    "depends": [
        "mail",
    ],
    "data": [
        "security/ir.model.access.csv",
        "data/sequence.xml",
        "views/patient_views.xml",
        "views/patient_readonly_views.xml",
        "views/appointment_views.xml",
        "views/menu.xml",
    ],
    'installable': True,
    'application': True,
}