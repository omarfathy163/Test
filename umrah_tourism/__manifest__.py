{
    "name": "Umrah & Tourism Management",
    "summary": "Manage travel agents, groups, services, visas, pilgrims, and portal for Umrah/Tourism",
    "version": "18.0.1.0.0",
    "category": "Services/Vertical",
    "author": "Sharks Tech",
    "website": "https://sharkstech.example",
    "license": "LGPL-3",
    "depends": ["base", "contacts", "portal", "mail", "account"],
    "data": [
        "security/umrah_security.xml",
        "security/ir.model.access.csv",
        "data/visa_types.xml",
        "views/menu.xml",
        "views/agent_views.xml",
        "views/agent_employee_views.xml",
        "views/service_views.xml",
        "views/contract_views.xml",
        "views/group_views.xml",
        "views/pilgrim_views.xml",
        "views/visa_views.xml",
        "views/portal_templates.xml"
    ],
    "assets": {
        "web.assets_frontend": [
            "/umrah_tourism/static/src/css/portal.css",
        ],
    },
    "application": True,
    "installable": True,
}
