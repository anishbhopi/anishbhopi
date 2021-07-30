# -*- coding: utf-8 -*-

from odoo import ,models, fields, api


# class college__mgmt(models.Model):
#     _name = 'college__mgmt.college__mgmt'
#     _description = 'college__mgmt.college__mgmt'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100




class CollegeStudent(models.Model):
    _name = "college.student"

    _description = "college student entry"
    name = feild.char('student name')
    mobile_No = feild.int ('student No.')