import base64
# import re
# from openerp import tools
# from openerp import SUPERUSER_ID
from openerp.osv import osv
# from openerp.osv import fields
# from openerp.tools.safe_eval import safe_eval as eval
# from openerp.tools.translate import _


class mail_compose_message(osv.TransientModel):
    _inherit = 'mail.compose.message'

    def send_mail(self, cr, uid, ids, context=None):
        """ Process the wizard content and proceed with sending the related
            email(s), rendering any template patterns on the fly if needed. """
        if context is None:
            context = {}
        ir_attachment_obj = self.pool.get('ir.attachment')
        active_ids = context.get('active_ids')
        is_log = context.get('mail_compose_log', False)

        for wizard in self.browse(cr, uid, ids, context=context):
            mass_mail_mode = wizard.composition_mode == 'mass_mail'
            active_model_pool_name = wizard.model\
                if wizard.model else 'mail.thread'
            active_model_pool = self.pool.get(active_model_pool_name)

            # wizard works in batch mode: [res_id] or active_ids
            res_ids = active_ids if mass_mail_mode and\
                wizard.model and active_ids else [wizard.res_id]
            for res_id in res_ids:
                # mail.message values, according to the wizard options
                post_values = {
                    'subject': wizard.subject,
                    'body': wizard.body,
                    'parent_id': wizard.parent_id and wizard.parent_id.id,
                    'partner_ids': [partner.id
                                    for partner in wizard.partner_ids],
                    'attachment_ids': [attach.id
                                       for attach in wizard.attachment_ids],
                    'attachments': [],
                }
                # mass mailing: render and override default values
                if mass_mail_mode and wizard.model:
                    email_dict = self.render_message(
                        cr, uid, wizard, res_id, context=context)
                    post_values[
                        'partner_ids'] += email_dict.pop('partner_ids', [])
                    for filename, attachment_data in \
                            email_dict.pop('attachments', []):
                        # decode as render message return in base64 while
                        # message_post expect binary
                        post_values['attachments'].append(
                            (filename, base64.b64decode(attachment_data)))
                    attachment_ids = []
                    for attach_id in post_values.pop('attachment_ids'):
                        new_attach_id = ir_attachment_obj.copy(
                            cr, uid, attach_id,
                            {'res_model': self._name,
                             'res_id': wizard.id},
                            context=context)
                        attachment_ids.append(new_attach_id)
                    post_values['attachment_ids'] = attachment_ids
                    post_values.update(email_dict)
                # post the message
                subtype = 'mail.mt_comment'
                if is_log:  # log a note: subtype is False
                    subtype = False
                # mass mail: is a log pushed to recipients, author not added
                elif mass_mail_mode:
                    subtype = False
                    # add context key to avoid subscribing the author
                    context = dict(context, mail_create_nosubscribe=True)
                msg_id = active_model_pool.message_post(
                    cr, uid, [res_id], type='comment',
                    subtype=subtype, context=context,
                    **post_values)
                # mass_mailing: notify specific partners, because subtype was
                # False, and no-one was notified
                if mass_mail_mode and\
                        post_values['partner_ids'] and\
                        not is_log:
                    self.pool.get('mail.notification')._notify(
                        cr, uid, msg_id, post_values['partner_ids'],
                        context=context)

        return {'type': 'ir.actions.act_window_close'}
