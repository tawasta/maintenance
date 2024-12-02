
from odoo import fields, models


class MaintenanceEquipmentDocument(models.Model):

    _name = 'maintenance.equipment.document'
    _description = 'Maintenance Equipment document'

    description = fields.Char(string="Description", copy=False)
    document_id = fields.Many2many("ir.attachment", string="Document", copy=False)
    equipment_id = fields.Many2one(comodel_name='maintenance.equipment', string="Equipment")
