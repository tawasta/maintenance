from odoo import api, fields, models


class MaintenanceEquipmentDocumentDocument(models.Model):
    _name = "maintenance.equipment.document.document"
    _description = "Maintenance Equipment Document document"
    _rec_name = "document_name"
    _order = "id desc, name desc"

    name = fields.Char(string="Document Name")
    description = fields.Char(string="Description", copy=False, required=True)
    document_id = fields.Many2many("ir.attachment", string="Document", copy=False)
    document_name = fields.Char(related="document_id.name")
    equipment_id = fields.Many2one(
        comodel_name="maintenance.equipment", string="Equipment"
    )

    def action_unlink(self):
        self.ensure_one()
        self.sudo().document_id.unlink()
        self.sudo().unlink()

    @api.model
    def create(self, values):
        """Set as Main document to an equipment if originally there are no
        documents linked to it."""
        set_as_main_document = False

        equipment_id = values.get("equipment_id", False)
        equipment = self.env["maintenance.equipment"].search(
            [("id", "=", equipment_id)]
        )

        if equipment and not equipment.document_document_ids:
            set_as_main_document = True

        resulting_record = super().create(values)

        if set_as_main_document:
            equipment.main_document_id = resulting_record

        return resulting_record
