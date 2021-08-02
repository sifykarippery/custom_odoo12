# -*- coding: utf-8 -*-

from odoo import models, fields, api
import logging
_logger = logging.getLogger(__name__)

class invoice_project(models.Model):
    _inherit ='account.invoice'

    project_id = fields.Many2one('project.project',string="Project_id")
    @api.multi
    def invoice_validate(self):
        res = super(invoice_project, self).invoice_validate()
        for invoice in self:
            project_name=invoice.partner_id.name+'_'+invoice.number
            project=invoice.env['project.project'].create({'name':project_name})
            invoice.project_id=project
            stages=invoice.env['project.task.type'].search([('name', 'in',['Meeting Stage','Purchase Stage','Handover Stage'])])
            for record in stages:
                record.write({
                    'project_ids': [(6, 0,[project.id])]
                })
        _logger.info('FYI:------PROJECT CREATED-------')
        return res
