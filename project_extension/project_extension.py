from openerp.osv import fields, osv
# from openerp.tools.translate import _

# inherit the project_project model to add some extra fields


class project_project(osv.osv):
    _inherit = 'project.project'
    _columns = {

        'intermediary_org_tutor_id': fields.many2one('res.partner',
                                                     "Intermediary Org.",
                                                     domain=[('is_company',
                                                              '=',
                                                              True)]),
        'host_org_tutor_id': fields.many2one('res.partner',
                                             "Host Organization Tutor",
                                             domain=[('is_company',
                                                      '=',
                                                      False)]),
        'host_org_representative_id': fields.many2one('res.partner',
                                                      "Host Representative",
                                                      domain=[('is_company',
                                                               '=',
                                                               False)]),
        'host_organization_id': fields.many2one('res.partner',
                                                "Host Organization",
                                                domain=[('is_company',
                                                         '=',
                                                         True)]),
        'sending_tutor_id': fields.many2one('res.partner',
                                            "Sending Org. Tutor",
                                            domain=[('is_company',
                                                     '=',
                                                     False)]),
        'trainee_id': fields.many2one('res.partner',
                                      "Trainee",
                                      domain=[('is_company', '=', False)]),
        'workflow': fields.html('Workflow'),
        'laguage_course_id': fields.many2one('project.project',
                                             "Language Course"),
        'work_time_description': fields.text('Work Time Description'),
        'accomodation_link': fields.char("Accomodation Link", length=32),
        'transfer': fields.boolean('Transfer'),
        'transfer_description': fields.text('Logistic  Info'),
        'job_id': fields.many2one('hr.job', "Job Title"),
        'work_assignment': fields.text("Work Assignment"),
        'long_note': fields.html('Long Note'),
        'mobility': fields.boolean('Mobility'),
        'survey': fields.related('job_id', 'survey_id',
                                 type='many2one',
                                 relation='survey',
                                 string='Survey'),
        'response': fields.integer("Response"),
        'survey_id': fields.many2one('survey', "Assessment form"),
        'assessment_form_link': fields.char("Assessment form", length=32),
        'survey_response': fields.integer("Response"),
        'intro_meeting_date': fields.date('Introduction Date'),
        'intro_metting_note': fields.text("Introduction meeting Note"),
        'hosting': fields.boolean('Hosting Info Here ?'),
        'arrival_date': fields.date('Arrival Date'),
        'departure_date': fields.date('Departure Date'),
        'score_1': fields.integer('Score 1'),
        'assessment_1': fields.text("Assessment 1"),
        'score_2': fields.integer('Score 2'),
        'assessment_2': fields.text("Assessment 2"),
        'score_3': fields.integer('Score 3'),
        'assessment_3': fields.text("Assessment 3"),
        'score_4': fields.integer('Score 4'),
        'assessment_4': fields.text("Assessment 4"),
        'score_5': fields.integer('Score 5'),
        'assessment_5': fields.text("Assessment 5"),
        'score_6': fields.integer('Score 6'),
        'assessment_6': fields.text("Assessment 6"),
        'score_7': fields.integer('Score 7'),
        'assessment_7': fields.text("Assessment 7"),
        'score_8': fields.integer('Score 8'),
        'assessment_8': fields.text("Assessment 8"),
        'score_9': fields.integer('Score 9'),
        'assessment_9': fields.text("Assessment 9"),
        'score_10': fields.integer('Score 10'),
        'assessment_10': fields.text("Assessment 10"),
        'connection_ids': fields.many2many('res.partner',
                                           'project_partner_rel',
                                           'project_id',
                                           'partner_id',
                                           'Connections',
                                           states={'close': [('readonly',
                                                              True)],
                                                   'cancelled': [('readonly',
                                                                  True)]},
                                           domain=[('is_company',
                                                    '=',
                                                    False)]),
    }
    _defaults = {
        'intro_meeting_date': fields.date.context_today
    }

    def onchange_job(self, cr, uid, ids, job, context=None):
        """
         Onchange of job ID select the corresponding Survey form

        """
        if context is None:
            context = {}
        if job:
            job_obj = self.pool.get('hr.job').browse(
                cr, uid, job, context=context)
            if job_obj.survey_id:
                return {'value': {'survey': job_obj.survey_id.id}}

        return {'value': {'survey': False}}

    def action_print_job_survey(self, cr, uid, ids, context=None):
        """
        If response is available then print this response
        otherwise print survey form(print template of the survey).

        @param self: The object pointer
        @param cr: the current row, from the database cursor,
        @param uid: the current user ID for security checks,
        @param ids: List of Survey IDs
        @param context: A standard dictionary for contextual values
        @return: Dictionary value for print survey form.
        """
        if context is None:
            context = {}
        record = self.browse(cr, uid, ids, context=context)
        record = record and record[0]
        context.update({'survey_id': record.survey.id, 'response_id': [
                       record.response], 'response_no': 0, })
        value = self.pool.get("survey").action_print_survey(
            cr, uid, ids, context=context)
        return value

    def action_print_survey(self, cr, uid, ids, context=None):
        """
        If response is available then print this response
        otherwise print survey form(print template of the survey).

        @param self: The object pointer
        @param cr: the current row, from the database cursor,
        @param uid: the current user ID for security checks,
        @param ids: List of Survey IDs
        @param context: A standard dictionary for contextual values
        @return: Dictionary value for print survey form.
        """
        if context is None:
            context = {}
        record = self.browse(cr, uid, ids, context=context)
        record = record and record[0]
        context.update({'survey_id': record.survey_id.id, 'response_id': [
                       record.survey_response], 'response_no': 0, })
        value = self.pool.get("survey").action_print_survey(
            cr, uid, ids, context=context)
        return value
