# -*- coding: utf-8 -*-
##############################################################################
#
#    Copyright (C) SHS-AV s.r.l. (<http://ww.zeroincombenze.it>)
#    All Rights Reserved
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

from openerp.osv import orm, fields

# X_PAYMENT_STATUS = [('1', 'in attesa'), ('2', 'da pagare'), ('3', 'in corso')
# , ('4', 'frazionato'), ('5', 'pagato'), ('6', 'riconciliato')]
X_PAYMENT_STATUS = [('1', '1'),
                    ('2', '2'),
                    ('3', '3'),
                    ('4', '4'),
                    ('5', '5'),
                    ('6', '6'),
                    ('7', '7'),
                    ('8', '8')]


class account_invoice(orm.Model):
    _inherit = "account.invoice"

    _columns = {
        'x_payment_status': fields.selection(
            X_PAYMENT_STATUS,
            'Stato pagamento',
            select=1,
            translate=False,
            store=True
        )
    }
