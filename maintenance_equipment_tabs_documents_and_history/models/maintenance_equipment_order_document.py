from odoo import fields, models


class MaintenanceEquipmentOrderDocument(models.Model):
    _name = "maintenance.equipment.order.document"
    _description = "Maintenance Equipment Order document"

    description = fields.Char(string="Description", copy=False, required=True)
    document_id = fields.Many2many("ir.attachment", string="Document", copy=False)
    equipment_id = fields.Many2one(
        comodel_name="maintenance.equipment", string="Equipment"
    )

    def action_unlink(self):
        self.ensure_one()
        self.sudo().document_id.unlink()
        self.sudo().unlink()
