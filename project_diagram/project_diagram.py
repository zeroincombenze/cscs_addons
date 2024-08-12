from openerp.osv import fields, osv
from dateutil.relativedelta import relativedelta
from openerp.tools.translate import _
from operator import itemgetter

_intervalTypes = {
    'hours': lambda interval: relativedelta(hours=interval),
    'days': lambda interval: relativedelta(days=interval),
    'months': lambda interval: relativedelta(months=interval),
    'years': lambda interval: relativedelta(years=interval),
}

DT_FMT = '%Y-%m-%d %H:%M:%S'

def dict_map(f, d):
    return dict((k, f(v)) for k,v in d.items())

def _find_fieldname(model, field):
    inherit_columns = dict_map(itemgetter(2), model._inherit_fields)
    all_columns = dict(inherit_columns, **model._columns)
    for fn in all_columns:
        if all_columns[fn] is field:
            return fn
    raise ValueError('Field not found: %r' % (field,))

class selection_converter(object):
    """Format the selection in the browse record objects"""
    def __init__(self, value):
        self._value = value
        self._str = value

    def set_value(self, cr, uid, _self_again, record, field, lang):
        # this design is terrible
        # search fieldname from the field
        fieldname = _find_fieldname(record._table, field)
        context = dict(lang=lang.code)
        fg = record._table.fields_get(cr, uid, [fieldname], context=context)
        selection = dict(fg[fieldname]['selection'])
        self._str = selection[self.value]

    @property
    def value(self):
        return self._value

    def __str__(self):
        return self._str

translate_selections = {
    'selection': selection_converter,
}



translate_selections = {
    'selection': selection_converter,
}


class project_task(osv.osv):
    _inherit = "project.task"
    _columns = {
             'to_ids': fields.one2many('project.task.transition',
                                            'task_from_id',
                                            'Next Task'),
             'from_ids': fields.one2many('project.task.transition',
                                            'task_to_id',
                                            'Previous Task'),
              }
              
project_task()              

class project_task_transition(osv.osv):
    _name = "project.task.transition"
    _description = "Task Transition"

    _interval_units = [
        ('hours', 'Hour(s)'), ('days', 'Day(s)'),
        ('months', 'Month(s)'), ('years','Year(s)')
    ]

    def _get_name(self, cr, uid, ids, fn, args, context=None):
        result = dict.fromkeys(ids, False)
        formatters = {
            'auto': _('Automatic transition'),
            'time': _('After %(interval_nbr)d %(interval_type)s'),
            'cosmetic': _('Cosmetic'),
        }
        for tr in self.browse(cr, uid, ids, context=context,
                              fields_process=translate_selections):
            result[tr.id] = formatters[tr.trigger.value] % tr
        return result
           
        


    def _delta(self, cr, uid, ids, context=None):
        assert len(ids) == 1
        transition = self.browse(cr, uid, ids[0], context=context)
        if transition.trigger != 'time':
            raise ValueError('Delta is only relevant for timed transition.')
        return relativedelta(**{str(transition.interval_type): transition.interval_nbr})


    _columns = {
        'name': fields.function(_get_name, string='Name',
                                type='char', size=128),
        'task_from_id': fields.many2one('project.task',
                                            'Previous Task', select=1,
                                            required=True, ondelete="cascade"),
        'task_to_id': fields.many2one('project.task',
                                          'Next Task',
                                          required=True, ondelete="cascade"),
        'interval_nbr': fields.integer('Interval Value', required=True),
        'interval_type': fields.selection(_interval_units, 'Interval Unit',
                                          required=True),

        'trigger': fields.selection([('auto', 'Automatic'),
                                     ('time', 'Time'),
                                     ('cosmetic', 'Cosmetic'),  # fake plastic transition
                                    ],
                                    'Trigger', required=True,
                                    help="How is the destination task triggered"),
    }

    _defaults = {
        'interval_nbr': 1,
        'interval_type': 'days',
        'trigger': 'time',
    }
    def _check_project(self, cr, uid, ids, context=None):
        for obj in self.browse(cr, uid, ids, context=context):
            if obj.task_from_id.project_id != obj.task_to_id.project_id:
                return False
        return True

    _constraints = [
            (_check_project, 'The To/From Task of transition must be of the same Project ', ['activity_from_id,activity_to_id']),
        ]

    _sql_constraints = [
        ('interval_positive', 'CHECK(interval_nbr >= 0)', 'The interval must be positive or zero')
    ]

project_task_transition()



