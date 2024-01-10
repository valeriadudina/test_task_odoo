from odoo import models, fields

class First_module(models.Model):
    _name = 'firstmodule.first'


    name = fields.Many2one('res.partner', string = 'Person name')
    class_id = fields.Integer(string = 'Class')
    division = fields.Char(string = 'Division')





