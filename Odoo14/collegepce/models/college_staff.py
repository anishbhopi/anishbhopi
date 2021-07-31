# -*- coding: utf-8 -*-
import datetime
from odoo import api, fields, models, _

class CollegeStaff(models.Model):
    _name = "college.staff"
    _description = "College Staff"

    employee_id = fields.Integer('Employee ID', required=0)

    first_name = fields.Char('First Name', default='', required=0)
    last_name = fields.Char('Last Name', default='', required=0)
    full_name = fields.Char('Full Name', compute='_compute_name', required=0)
    @api.depends('first_name', 'last_name')
    def _compute_name(self):
        for record in self:
            record.full_name = record.first_name or "" + " " + record.last_name or ""


    dob = fields.Date('Date of Birth', required=0)
    age = fields.Char('Age', compute="get_age", required=0)

    @api.depends('dob')
    def get_age(self):
        today_date = datetime.date.today()
        for staff in self:
            if staff.dob:
                dob = fields.Datetime.to_datetime(staff.dob).date()
                total_age = str(int((today_date - dob).days / 365))
                staff.age = total_age
            else:
                staff.age = "Please enter Date of Birth"
    gender = fields.Selection([
        ('male', 'Male'),
        ('female', 'Female')],
        'Gender', default='', required=0)
    email = fields.Char('Email ID', default='', required=0)
    phone_number = fields.Integer('Phone No', required=0)
    permanent_address = fields.Char('Permanent Address', default='', required=0)
    temporary_address = fields.Char('Temporary Address', default='', required=0)

    marital_status = fields.Selection([
        ('married', 'Married'),
        ('unmarried', 'Unmarried'),
        ('divorce', 'Divorce')],
        'Marital Status', default='', required=0)





    blood_group = fields.Selection([
        ('a+', 'A+'),
        ('a-', 'A-'),
        ('b+', 'B+'),
        ('b-', 'B-'),
        ('o+', 'O+'),
        ('o-', 'O-'),
        ('ab+', 'AB+'),
        ('ab-', 'AB-')],
    'Blood Group', default = '', required = 0)






    #photo

    nationality = fields.Char('Nationality', default='', required=0)
    religion = fields.Char('Religion', default='', required=0)

    employee_status = fields.Selection([
        ('fulltime', 'Full Time '),
        ('parttime', 'Part Time')],
        'Employee Status', default = '', required = 0)

    education_qualification = fields.Selection([
        ('bachelor', 'Bachelor'),
        ('masters', 'Masters'),
        ('phd', 'PHD')],


default = '', required = 0)

    department = fields.Selection([
        ('it', 'Information Technology'),
        ('cs', 'Computer Science'),
        ('at', 'Automobile Engineering'),
        ('cv', 'Civil Engineering'),
        ('mech', 'Mechanical Engineering'),
        ('extc', 'Electronics and Communication')],

   required = 0)



date_of_joining = fields.Date(string="Date of Joining", default=fields.Date.today())

experience = fields.Integer('Experience')
bank_account_number = fields.Integer('Bank Account Number', required=0)
aadhar_no = fields.Integer('Aadhar Number', default='', required=0)
fellowship = fields.Boolean('Fellowship', default=False, required=0)
















