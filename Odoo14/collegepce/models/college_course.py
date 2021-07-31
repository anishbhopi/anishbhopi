# -*- coding: utf-8 -*-
import datetime
from odoo import api, fields, models, _

class CollegeCourse(models.Model):
    _name = "college.course"
    _description = "College Course"

    course_name = fields.Char('Course Name', default='', required=1)
    course_code = fields.Char('Course Code', default='', required=1)
    active = fields.Boolean('Active')
    course_duration = fields.Integer('Course Duration')
    course_department =  fields.Selection([
        ('CE', 'Computer Engineering'),
        ('ME', 'Mechanical Engineering'),
        ('EC', 'Electronics & Communications'),
        ('EE', 'Electrical Engineering'),
        ('CIE', 'Civil Engineering'),],
        'Department', default='CE', required=1)
    #course_teacher = Many2one
    #course_student = Many2one
    course_fees = fields.Integer('Course Fees')
    course_intake = fields.Integer('Course Intake')


