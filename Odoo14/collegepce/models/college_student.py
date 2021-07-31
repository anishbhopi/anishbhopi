# -*- coding: utf-8 -*-
import datetime
from odoo import api, fields, models, _

class CollegeStudent(models.Model):
    _name = "college.student"
    _description = "College Student"

    first_name = fields.Char('First Name', default='', required=0)
    last_name = fields.Char('Last Name', default='', required=0)
    full_name = fields.Char('Full Name', compute='_compute_name', required=0)
    @api.depends('first_name', 'last_name')
    def _compute_name(self):
        for record in self:
            record.full_name = record.first_name or "" + " " + record.last_name or ""

    dob = fields.Date('Date of Birth',required=0)
    age = fields.Char('Age', compute="get_age", required=0)

    @api.depends('dob')
    def get_age(self):
        today_date = datetime.date.today()
        for student in self:
            if student.dob:
                dob = fields.Datetime.to_datetime(student.dob).date()
                total_age = str(int((today_date - dob).days / 365))
                student.age = total_age
            else:
                 student.age = "Please enter Date of Birth"

    education_qualification = fields.Selection([
        ('bachelor', 'Bachelor'),
        ('masters', 'Masters'),
        ('phd', 'PHD')],
        'Gender', default='', required=0)
    gender = fields.Selection([
        ('male', 'Male'),
        ('female', 'Female')],
        'Gender', default='', required=0)
    email = fields.Char('Email ID', default='', required=0)
    phone_number = fields.Integer('Phone No', required=0)
    permanent_address = fields.Char('Permanent Address', default='', required=0)
    temporary_address = fields.Char('Temporary Address', default='', required=0)
    enrollment_no = fields.Integer('Enrollment No', required=0)
    fathers_name = fields.Char("Father's name", required=0)
    mothers_name = fields.Char("Mother's name", required=0)
    ssc_percentage = fields.Float('SSC Percentage', required=0)
    hsc_diploma = fields.Selection([
        ('hsc', 'HSC'),
        ('diploma', 'Diploma')],
        'HSC/Diploma', default='', required=0)
    percentage = fields.Float('HSC/Diploma Percentage', required=0)
    blood_group = fields.Selection([
        ('a+', 'A+'),
        ('a-', 'A-'),
        ('b+', 'B+'),
        ('b-', 'B-'),
        ('o+', 'O+'),
        ('o-', 'O-'),
        ('ab+', 'AB+'),
        ('ab-', 'AB-')],
        'Blood Group', default='', required=0)
    scholarship = fields.Boolean('Scholarship', default=False, required=0)
    disabled = fields.Boolean('Differently abled', default=False, required=0)
    emergency_number = fields.Integer('Emergency Contact Number', required=0)
    #photo
    date_of_joining = fields.Date(string="Date of Joining", default=fields.Date.today())
    nationality = fields.Char('Nationality', default='', required=0)
    religion = fields.Char('Religion', default='', required=0)
    aadhar_no = fields.Integer('Aadhar Number', default='', required=0)
    date_of_joining = fields.Date(string="Date of Joining", default=fields.Date.today())



