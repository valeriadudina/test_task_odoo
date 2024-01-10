from odoo import models, fields, api

class Wizard_task(models.Model):
    _name = "wizard.task"

    name = fields.Char(string = "name")
    is_company = fields.Boolean(string="is_company")


    def action_create_person(self):
        return {
            "res_model": "res.partner",
            "type": "ir.actions.act_window",
            "view_mode": "form",
            "view_id": self.env.ref("base.view_partner_form").id
        }
    def action_create_company(self):
        return {
            "res_model": "res.partner",
            "type": "ir.actions.act_window",
            "view_mode": "form",
            "view_id": self.env.ref("base.view_partner_form").id,
            "context": {"default_is_company": True}
        }
    def action_create_partner(self):
        return {
            "res_model": "wizard.task",
            "type": "ir.actions.act_window",
            "view_mode": "form",
            "view_id": self.env.ref("first_module.wizard_task_form_modal").id

        }
