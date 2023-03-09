from odoo import api, fields, models
from odoo.osv import expression


class ProductProduct(models.Model):
    _inherit = "product.product"

    @api.model
    def _name_search(self, name="", args=None, operator="ilike", limit=100, name_get_uid=None):
        args = args or []
        domain = []
        if name:
            domain = ["|", ("name", operator, name), ("description_sale", operator, name), ("default_code", operator, name)]
        product_ids = self._search(expression.AND([domain, args]), limit=limit, access_rights_uid=name_get_uid)
        if product_ids:
            return product_ids

        return super(ProductProduct, self)._name_search(
            name, args=args, operator=operator, limit=limit, name_get_uid=name_get_uid
        )
