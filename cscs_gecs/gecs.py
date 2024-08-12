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
from openerp.osv import fields, osv
from openerp.tools.translate import _


class gecs(osv.osv):
    _name = 'res.partner'
    _inherit ='res.partner'
    
    _columns = {
        'X_GECS_ID': fields.integer('X_GECS_ID', size=128),
        'text_GECS' : fields.text('text_GECS'),
        'X_GECS_codfisc': fields.char('X_GECS_codfisc', size=32),
        'X_GECS_surname' : fields.char ('X_GECS_surname' , size=128) ,
        'X_GECS_firstname' : fields.char ('X_GECS_firstname' , size=128),
        'X_gecs_partner_phone2' : fields.char ('X_gecs_partner_phone2' , size=50),
        'X_GECS_sex' : fields.char ('X_GECS_sex' , size=1),
        'vat_2' : fields.char ('vat_2' , size=128),
    }
gecs()