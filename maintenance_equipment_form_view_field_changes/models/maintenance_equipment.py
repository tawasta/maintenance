from odoo import fields, models


class MaintenanceEquipment(models.Model):
    _inherit = "maintenance.equipment"

    description = fields.Text(string="Description", copy=False)
    engine = fields.Text(string="Engine", copy=False)
    owner_id = fields.Many2one(
        string="Owner", comodel_name="res.partner", copy=False, store=True
    )
