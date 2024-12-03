from odoo import fields, models


class MaintenanceEquipmentDocumentDocument(models.Model):
    _name = "maintenance.equipment.document.document"
    _description = "Maintenance Equipment Document document"
    _rec_name = "document_name"

    name = fields.Char(string="Document Name")
    description = fields.Char(string="Description", copy=False)
    document_id = fields.Many2many(
        "ir.attachment", string="Document", copy=False, required=True
    )
    document_name = fields.Char(related="document_id.name")
    equipment_id = fields.Many2one(
        comodel_name="maintenance.equipment", string="Equipment"
    )

    def action_unlink(self):
        self.ensure_one()
        self.sudo().document_id.unlink()
        self.sudo().unlink()
