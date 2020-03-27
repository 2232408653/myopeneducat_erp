# -*- coding: utf-8 -*-
###############################################################################
#
#    Tech-Receptives Solutions Pvt. Ltd.
#    Copyright (C) 2009-TODAY Tech-Receptives(<http://www.techreceptives.com>).
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Lesser General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Lesser General Public License for more details.
#
#    You should have received a copy of the GNU Lesser General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
###############################################################################

from odoo import models, fields, api


class OpDepartment(models.Model):
    _name = "op.department"
    _description = "开源教育 院系"

    name = fields.Char('名称')
    code = fields.Char('编号')
    parent_id = fields.Many2one('op.department', '父部门')

    @api.model
    #客制化create方法
    def create(self, vals):
        department = super(OpDepartment, self).create(vals)
        self.env.user.write({'department_ids': [(4, department.id)]})
        return department
