# -*- coding: utf-8 -*- 
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).

from odoo import api, fields, models, tools, _
from odoo.exceptions import UserError,ValidationError
from datetime import date
import base64
from collections import defaultdict
from odoo.addons import decimal_precision as dp
from odoo.tools.float_utils import float_compare

class ProductTemplate(models.Model):
	_inherit = 'product.template'

	@api.constrains('tracking')
	def check_tmpl_tracking(self):
		for prod in self:
			if prod.product_variant_ids:
				for variant in prod.product_variant_ids:
					lot_ids = self.env['stock.production.lot'].search([('product_id','=',variant.id)])
					if lot_ids:
						raise ValidationError('El producto ya tiene asignado nros de serie.')
