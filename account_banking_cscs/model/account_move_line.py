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
from operator import itemgetter


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


class account_move_line(orm.Model):
    _inherit = 'account.move.line'

    def _x_payment_status(self, cr, uid, ids, name, arg=None, context=None):
        """Customize CSCS"""
        if not ids:
            return {}
        cr.execute("""select d.id,i.x_payment_status
                   from account_move_line d inner join account_move h
                   on d.move_id=h.id
                   left join account_invoice i on i.move_id=h.id
                   where d.id in %s""", (tuple(ids),))
        r = dict(cr.fetchall())
        return r

    def _x_payment_search(self, cr, uid, obj, name, args, context=None):
        if not args:
            return []
        sql_args = tuple(map(itemgetter(2), args))
        cr.execute("""select d.id,i.x_payment_status
                   from account_move_line d inner join account_move h
                   on d.move_id=h.id
                   left join account_invoice i on i.move_id=h.id
                   where %s""", sql_args)
        res = cr.fetchall()
        if not res:
            return [('id', '=', '0')]
        return [('id', 'in', map(lambda x:x[0], res))]

    _columns = {
        # 'x_payment_status': fields.function(
        #     _x_payment_status,
        #     type='selection',
        #     selection=X_PAYMENT_STATUS,
        #     string='Stato pagamento',
        #     readonly=False,
        #     select=1,
        #     translate=True,
        #     store=True
        #     # fnct_search=_x_payment_search
        'x_payment_status': fields.selection(
            X_PAYMENT_STATUS,
            string='Stato pagamento',
            readonly=False,
            select=1,
            translate=False,
            store=True
        )
    }
