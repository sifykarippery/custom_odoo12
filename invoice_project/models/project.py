from odoo import models, fields, api

class purchase_project(models.Model):
    _inherit='purchase.order'
    project_id=fields.Many2one('project.project',string='project_id')
class stock_project(models.Model):
    _inherit='stock.picking'
    project_id = fields.Many2one('project.project', string='project_id')

class project_task_stages(models.Model):
    _inherit='project.task'

    stage_check_purchase=fields.Boolean(compute='check_stage',store=True)
    stage_check_handover=fields.Boolean(compute='check_stage_handover',store=True)

    @api.depends('stage_id')
    def check_stage(self):

        if self.stage_id.name =='Purchase Stage':
           self.stage_check_purchase=True
        else:
            self.stage_check_purchase=False

    @api.depends('stage_id')
    def check_stage_handover(self):
        if self.stage_id.name == 'Handover Stage':
           self.stage_check_handover=True
        else:
            self.stage_check_handover=False

    def action_view_purchase_order(self):

        return {
                'name': 'Purchase Order',
                'view_type': 'form',
                'view_mode': 'tree,form',
                'res_model': 'purchase.order',
                'view_id': False,
                'type': 'ir.actions.act_window',
                'domain': [('id', 'in', [self.project_id.id])],
                 'target': 'current',


            }

    def action_view_delivery_order(self):
        return {
            'name':'Delivery order',
            'view_type': 'form',
            'view_mode': 'tree,form',
            'res_model': 'stock.picking',
            # 'view_id': 'stock.picking.stock.vpicktree',
            'type': 'ir.actions.act_window',
            'domain': [('id', 'in', [self.project_id.id])],
            'target': 'current',

        }