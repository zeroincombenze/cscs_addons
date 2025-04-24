# -*- coding: utf-8 -*-
# Copyright 2017 Antonio M. Vigliotti <antoniomaria.vigliotti@gmail.com>
#                Odoo Italian Community
#                Odoo Community Association (OCA)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
{
    'name': "bank_payment_order",

    'summary': """Credit Transfer Payment Order""",

    'description': """(en)

Credit Transfer Payment Order
=============================

This module adds support for credit transfer payment orders.

Installation
------------

This module depends on:

- account_payment_partner
- base_iban

Usage
-----

No yet documented


(it)
Ordini di pagamento tramite bonifico
====================================

Questo modulo gestisce gli ordini di pagamento tramite bonifico Sepa.
    """,

    'author': "SHS-AV s.r.l.",
    'website': "https://www.zeroincombenze.it/",

    'category': 'Banking addons',
    'version': '7.0.0.1.0',
    'depends': [
        'base_iban',
    ],
    'data': [
        "security/ir.model.access.csv",
    ],
    "qweb": [],
    "demo": [],
    "test": [],
    "active": False,
    'installable': True
}
