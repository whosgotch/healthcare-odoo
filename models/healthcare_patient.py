from odoo import models, fields

class HealthcarePatient(models.Model):
    _name = "healthcare.patient"
    _description = "Patient"

    full_name = fields.Char(string="Full Name", required=True)
    gender = fields.Selection([('female', 'Female'), ('male', 'Male')]) 
    date_of_birth = fields.Date(string="Date of Birth")
    age = fields.Integer(string="Age")
    passport_data = fields.Char(string="Passport Data")
    contact_address = fields.Char(string="Contact Address")