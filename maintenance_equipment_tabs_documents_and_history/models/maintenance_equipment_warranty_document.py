from odoo import fields, models


class MaintenanceEquipmentWarrantyDocument(models.Model):
    _name = "maintenance.equipment.warranty.document"
    _description = "Maintenance Equipment Warranty document"

    description = fields.Char(string="Description", copy=False)
    document_id = fields.Many2many(
        "ir.attachment", string="Document", copy=False, required=True
    )
    equipment_id = fields.Many2one(
        comodel_name="maintenance.equipment", string="Equipment"
    )

    def action_unlink(self):
        self.ensure_one()
        self.sudo().document_id.unlink()
        self.sudo().unlink()
