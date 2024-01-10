from odoo import models, fields, api

class Wizard_task(models.TransientModel):
    _name = "wizard.task.wizard"

    name = fields.Char(string = "name")
    is_company = fields.Boolean(string="is_company")