
from odoo import fields, models


class MaintenanceEquipment(models.Model):

    _inherit = 'maintenance.equipment'

    delivery_date = fields.Date(string="Delivery Date", copy=False)
    maintenance_alarm_date = fields.Date(string="Maintenance Alarm", copy=False)
    order_status = fields.Selection(
        selection=[("ordered", "Ordered"), ("delivered", "Delivered")],
        default="ordered",
        help="Equipment is shown as red when 'Ordered' has been selected.",
    )
    order_document_ids = fields.One2many(
        "maintenance.equipment.order.document",
        "equipment_id",
        string="Order Documents",
        copy=False
    )
    picture_document_ids = fields.One2many(
        "maintenance.equipment.picture.document",
        "equipment_id",
        string="Pictures",
        copy=False
    )
    document_ids = fields.One2many(
        "maintenance.equipment.document",
        "equipment_id",
        string="Documents",
        copy=False
    )
