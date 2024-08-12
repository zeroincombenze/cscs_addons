# -*- coding: utf-8 -*-
# Copyright 2016 Antonio M. Vigliotti <antoniomaria.vigliotti@gmail.com>
#                Odoo Italian Community
#                Odoo Community Association (OCA)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
{
    'name': "cscs_task_cv",

    'summary': """Manage CV in task""",

    'description': """
Add specific fields to project.task to manage CV
------------------------------------------------

    "Number" integer NOT NULL,
    "Surname" varchar(160) DEFAULT NULL,
    "Firstname" varchar(160) DEFAULT NULL,
    "Sex" varchar(40) DEFAULT NULL,
    "Nationality" varchar(100) DEFAULT NULL,
    "DatePlaceofBirth" varchar(100) DEFAULT NULL,
    "Language" text ,
    "CountriesofExp" text ,
    "DonorsClients" text ,
    "KeyQualifications" text ,
    "Education" text ,
    "EmploymentHist" text ,
    "Address" varchar(160) DEFAULT NULL,
    "Email" varchar(160) DEFAULT NULL,
    "Fax" varchar(160) DEFAULT NULL,
    "Phone" varchar(160) DEFAULT NULL,
    "Remarks" text ,
    "file1" varchar(160) DEFAULT NULL,
    "file2" varchar(160) DEFAULT NULL,
    "file3" varchar(160) DEFAULT NULL,
    "file4" varchar(160) DEFAULT NULL,
    "file1" varchar(160) DEFAULT NULL,
    "file2" varchar(160) DEFAULT NULL,
    "file3" varchar(160) DEFAULT NULL,
    "file4" varchar(160) DEFAULT NULL,
    "file1_mimetype" varchar(128) DEFAULT NULL,
    "file2_mimetype" varchar(128) DEFAULT NULL,
    "file3_mimetype" varchar(128) DEFAULT NULL,
    "file4_mimetype" varchar(128) DEFAULT NULL,
    """,

    'author': "SHS-AV s.r.l.",
    'website': "https://www.zeroincombenze.it/",

    'category': 'Generic Modules/Accounting',
    'version': '7.0.0.1.0',

    # any module necessary for this one to work correctly
    'depends': ['project'],

    # always loaded
    'data': [
        "security/ir.model.access.csv",
    ],
    "qweb": [],
    "demo": [],
    "test": [],
    "active": False,
    'installable': True
}
