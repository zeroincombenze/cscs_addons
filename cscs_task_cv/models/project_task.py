# -*- coding: utf-8 -*-
# Copyright 2016 Antonio M. Vigliotti <antoniomaria.vigliotti@gmail.com>
#                Odoo Italian Community
#                Odoo Community Association (OCA)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from osv import osv, fields


class project_task(osv.Model):
    _inherit = 'project.task'

    _columns = {
        'cv_number': fields.integer('Prior id',
                                    required=True),
        'cv_sex': fields.char('Sex'),
        'cv_nationality': fields.char('Candidate country'),
        'cv_dateplaceofbirth': fields.char('Candidate date and place of Birth'),
        'cv_language': fields.char('Candidate language'),
        'cv_countriesofexp': fields.char('Candidate countries of experince'),
        'cv_donorsclients': fields.char('Donors'),
        'cv_keyqualifications': fields.char('Candidate key qualification'),
        'cv_education': fields.char('Candidate Education'),
        'cv_employmenthist': fields.char('Candidate Employment History'),
        'cv_address': fields.char('Candidate Address'),
        'cv_email': fields.char('Candidate e-mail'),
        'cv_fax': fields.char('Candidate fax number'),
        'cv_phone': fields.char('Candidate phone number'),
        'cv_remarks': fields.char('Remarks'),
        'cv_file1': fields.char('Attachment n.1'),
        'cv_file2': fields.char('Attachment n.2'),
        'cv_file3': fields.char('Attachment n.3'),
        'cv_file4': fields.char('Attachment n.4'),
        'cv_file1_mimetype': fields.char('Attachment n.1 mimetype'),
        'cv_file2_mimetype': fields.char('Attachment n.2 mimetype'),
        'cv_file3_mimetype': fields.char('Attachment n.3 mimetype'),
        'cv_file4_mimetype': fields.char('Attachment n.4 mimetype'),
    }
