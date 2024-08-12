# -*- coding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2004-2010 Tiny SPRL (<http://tiny.be>).
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################

{
    'name': 'CSCS - Project Extension',
    'version': '1.2',
    'author': 'CSCS',
    'website': 'http://www.cscs.it/',
    'category': 'Project Management',
    'sequence': 1,
    'summary': 'Added additional information to project master for CSCS',
    'images': [
    ],
    'depends': [
        'project',
        'hr',
        'survey',
        'sale',
        'crm'

    ],
    'description': """
        New fields added to project master

    """,
    'data': [
        'security/message_security.xml',
        'project_extension_view.xml',
        'mass_log_note_view.xml',
        'mail_message_view.xml',

    ],
    'demo': [],
    'test': [

    ],
    'installable': True,
    'auto_install': False,
    'application': True,
    'css': [],
    'js': [],
}
# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
