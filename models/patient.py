from odoo import models, fields, api
from dateutil.relativedelta import relativedelta
from datetime import date


class HospitalPatient(models.Model):
    _name = 'hospital.patient'
    _inherit = ['mail.thread']
    _description = 'Gestión de pacientes'
    _rec_name = 'partner_id'
    
    partner_id = fields.Many2one('res.partner', string='Nombre', required=True, ondelete='restrict', tracking=True)
    phone = fields.Char(string='Teléfono', tracking=True)
    date_of_birth = fields.Date(string='Fecha de nacimiento', tracking=True)
    age = fields.Char(string='Edad', compute='_compute_age', store=True)
    gender = fields.Selection([('male', 'Masculino'), ('female', 'Femenino')], string='Género', tracking=True)
    blood_group = fields.Selection([
        ('A+', 'A+'), ('A-', 'A-'), ('B+', 'B+'), ('B-', 'B-'), 
        ('O+', 'O+'), ('O-', 'O-'), ('AB+', 'AB+'), ('AB-', 'AB-'),
    ], string='Grupo sanguíneo', tracking=True)

    @api.depends('date_of_birth')
    def _compute_age(self):
        for record in self:
            if record.date_of_birth:
                today = date.today()
                dob = record.date_of_birth
                delta = relativedelta(today, dob)
                years = delta.years
                months = delta.months
                days = delta.days
                record.age = f"{years} años, {months} meses y {days} días"
            else:
                record.age = "0 años, 0 meses y 0 días"