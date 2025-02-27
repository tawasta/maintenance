from odoo import api, fields, models


class MaintenanceEquipment(models.Model):
    _inherit = "maintenance.equipment"

    delivery_date = fields.Date(string="Delivery Date", copy=False)
    maintenance_alarm_date = fields.Date(string="Maintenance Alarm", copy=False)
    order_status = fields.Selection(
        selection=[("ordered", "Ordered"), ("delivered", "Delivered")],
        default="",
        help="Equipment is shown as red when 'Ordered' has been selected.",
    )
    order_document_ids = fields.One2many(
        "maintenance.equipment.order.document",
        "equipment_id",
        string="Order Documents",
        copy=False,
    )
    picture_document_ids = fields.One2many(
        "maintenance.equipment.picture.document",
        "equipment_id",
        string="Pictures",
        copy=False,
    )
    warranty_document_ids = fields.One2many(
        "maintenance.equipment.warranty.document",
        "equipment_id",
        string="Warranty documents",
        copy=False,
    )
    other_document_ids = fields.One2many(
        "maintenance.equipment.other.document",
        "equipment_id",
        string="Other documents",
        copy=False,
    )
    document_document_ids = fields.One2many(
        "maintenance.equipment.document.document",
        "equipment_id",
        string="Documents",
        copy=False,
    )
    main_document_id = fields.Many2one(
        comodel_name="maintenance.equipment.document.document",
        string="Main document",
        domain="[('id', 'in', document_document_ids)]",
        copy=False,
    )
    main_document_attach_id = fields.Many2one(
        "ir.attachment",
        compute="_compute_main_document_attach_id",
        store=True,
        copy=False,
    )

    @api.depends("main_document_id", "main_document_attach_id")
    def _compute_main_document_attach_id(self):
        for equip in self:
            if equip.main_document_id:
                equip.main_document_attach_id = equip.main_document_id.document_id
            else:
                equip.main_document_attach_id = False

    def download_file(self):
        for equip in self:
            if equip.main_document_attach_id:
                return {
                    "type": "ir.actions.act_url",
                    "url": "/web/content/{}?download=true".format(
                        equip.main_document_attach_id.id
                    ),
                    "target": "self",
                }
