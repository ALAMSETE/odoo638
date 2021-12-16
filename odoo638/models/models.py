# -*- coding: utf-8 -*-

from odoo import models, fields, api

class camiones638(models.Model):
	_name = 'odoo638.camiones638'
	_description = 'model camiones638'

	name = fields.Char('Matricula',required=True)
	marca = fields.Char(string='Marca',required=True)
	modelo = fields.Char(string='Modelo',required=True)
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
