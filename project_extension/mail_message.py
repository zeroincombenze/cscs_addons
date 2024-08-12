from openerp.osv import osv
from openerp.osv import fields


class mail_message(osv.Model):
    _inherit = 'mail.message'

    MODEL_LX = [('partner', 'Partners'),
                ('project', 'Projects'),
                ('invoice', 'Invoices'),
                # ('invoice_c', 'Invoices (customers)'),
                # ('invoice_p', 'Invoices (purchases)'),
                ('lead', 'Leads'),
                ('order', 'Sale Orders'),
                ('analytic_account', 'Analytic Accounts'),
                ('voucher', 'Vouchers')]

    def _get_record(self, cr, uid, ids, field_name, arg, context=None):
        res = {}
        for msg in self.browse(cr, uid, ids, context=context):
            res[msg.id] = True
            if msg.model and msg.res_id:
                rec = self.pool.get(msg.model).browse(
                    cr, uid, msg.res_id, context=context)
                if rec and 'name' in rec and rec.name:
                    res[msg.id] = rec.name
        return res
    _columns = {
        'id_papaer': fields.char('Paper ID', size=16),
        'security_level': fields.selection([('1', 'Level 1'),
                                            ('2', 'Level 2'),
                                            ('3', 'Level 3'), ], 'Level'),
        'model_selection': fields.selection(MODEL_LX, 'Linked To'),
        'sel_partner_id': fields.many2one('res.partner', 'Partner'),
        'sel_project_id': fields.many2one('project.project', 'Project'),
        'sel_invoice_id': fields.many2one('account.invoice', 'Invoice'),
        'sel_lead_id': fields.many2one('crm.lead', 'Lead'),
        'sel_order_id': fields.many2one('sale.order', 'Order'),
        'sel_analytic_account_id': fields.many2one('account.analytic.account',
                                                   'Analytic Account'),
        'sel_voucher_id': fields.many2one('account.voucher', 'Voucher'),
        'sel_record_name':
            fields.function(_get_record,
                            # fnct_search=_search_id,
                            string='Record',
                            type='char',
                            store={'mail.message':
                                   (lambda self,
                                    cr, uid, ids,
                                    c={}: ids,
                                    ['model', 'res_id'], 10), }),
    }
    _defaults = {'security_level': '1', }
    # 'model_selection': 'invoice'}

    def onchange_model(self, cr, uid, ids, model, context=None):
        v = {'sel_partner_id': False,
             'sel_project_id': False,
             'sel_invoice_id': False,
             'sel_lead_id': False,
             'sel_order_id': False,
             'sel_analytic_account_id': False,
             'sel_voucher_id': False}
        d = None

        if model:
            if model == 'partner':
                v['model'] = 'res.partner'
            elif model == 'project':
                v['model'] = 'project.project'
            elif model == 'invoice':
                # d['domain'] = {'model': [('state', '!=', 'draft')]}
                v['model'] = 'account.invoice'
            elif model == 'invoice_c':
                # d['domain'] = {'model': [('type', '=', 'out_invoice'),
                #                            ('state', '=', 'draft')]}
                v['model'] = 'account.invoice'
            elif model == 'invoice_p':
                # d['domain'] = {'model': [('type', '=', 'in_invoice',
                #                             ('state', '=', 'draft'))]}
                v['model'] = 'account.invoice'
            elif model == 'lead':
                v['model'] = 'crm.lead'
            elif model == 'order':
                v['model'] = 'sale.order'
            elif model == 'analytic_account':
                v['model'] = 'account.analytic.account'
            elif model == 'voucher':
                v['model'] = 'account.voucher'
        if d:
            return {'value': v, 'domain': d}
        return {'value': v}

    def onchange_sel_id(self, cr, uid, ids, res_id, context=None):
        v = {}
        if res_id:
            v['res_id'] = res_id
        return {'value': v}

    def create(self, cr, uid, vals, context=None):
        if vals.get('model', False) and\
                vals.get('res_id', False) and\
                not vals.get('model_selection', False):
            if vals['model'] == 'res.partner':
                vals['model_selection'] = 'partner'
                vals['sel_partner_id'] = vals['res_id']
            elif vals['model'] == 'project.project':
                vals['model_selection'] = 'project'
                vals['sel_project_id'] = vals['res_id']
            elif vals['model'] == 'account.invoice':
                vals['model_selection'] = 'invoice'
                vals['sel_invoice_id'] = vals['res_id']
            elif vals['model'] == 'crm.lead':
                vals['model_selection'] = 'lead'
                vals['sel_lead_id'] = vals['res_id']
            elif vals['model'] == 'sale.order':
                vals['model_selection'] = 'order'
                vals['sel_order_id'] = vals['res_id']
            elif vals['model'] == 'account.analytic.account':
                vals['model_selection'] = 'analytic_account'
                vals['sel_analytic_account_id'] = vals['res_id']
            elif vals['model'] == 'account.voucher':
                vals['model_selection'] = 'voucher'
                vals['sel_voucher_id'] = vals['res_id']
        print vals
        res = super(mail_message, self).create(cr, uid, vals, context)
        return res
