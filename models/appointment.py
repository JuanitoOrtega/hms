from odoo import models, fields, api
import pytz


class HospitalAppointment(models.Model):
    _name = 'hospital.appointment'
    _inherit = ['mail.thread']
    _description = 'Gestión de citas'
    _rec_name = 'patient_id'
    
    reference = fields.Char(string='Referencia', required=True, index='trigram', copy=False, default='Nuevo')
    patient_id = fields.Many2one('hospital.patient', string='Paciente', required=True, ondelete='restrict', tracking=True)
    datetime_appointment = fields.Datetime(string='Fecha y hora de la cita', required=True, tracking=True)
    note = fields.Text(string='Nota', tracking=True)
    state = fields.Selection([
        ('draft', 'Borrador'),
        ('confirmed', 'Confirmado'),
        ('progress', 'En progreso'),
        ('done', 'Hecho'),
        ('canceled', 'Cancelado'),
    ], string='Estado', required=True, default='draft', tracking=True)
    
    @api.model_create_multi
    def create(self, vals_list):
        for vals in vals_list:
            if not vals.get('reference') or vals['reference'] == 'Nuevo':
                vals['reference'] = self.env['ir.sequence'].next_by_code('hospital.appointment') or 'Nuevo'
        return super().create(vals_list)
    
    def action_confirm(self):
        for rec in self:
            rec.state = 'confirmed'