# -*- coding: utf-8 -*-

from odoo import models, fields, api
class SaleOrder(models.Model):
    _inherit= 'sale.order'
    _description = 'Sale Order'

    due_amount = fields.Float('Due amount', compute="default_payment_method_id")

    @api.depends("partner_id")
    def default_payment_method_id(self):
        date = fields.Date.today()
        self.due_amount = 0
        total=0
        obj = self.env['account.move.line'].search([('partner_id', '=', self.partner_id.id),('date', '=', date)])
        for i in obj:
            if i.move_id.state =="posted":
                if i.reconciled==False and i.balance !=0:
                    if i.account_id.reconcile ==True:
                        if i.account_id.internal_type in ['payable' ,'receivable']:
                            print("i.partner_id.name",i.balance)
                            total=total+i.balance
        self.due_amount = total




class AccountMove(models.Model):
    _inherit= 'account.move'
    _description = 'Account Move'


    due_amount= fields.Float('Due amount',compute="default_payment_method_id")

    @api.depends("partner_id")
    def default_payment_method_id(self):
        date = fields.Date.today()
        self.due_amount=0
        total = 0
        obj = self.env['account.move.line'].search([('partner_id', '=', self.partner_id.id),('date', '=', date)])
        for i in obj:
            if i.move_id.state =="posted":
                if i.reconciled==False and i.balance !=0:
                    if i.account_id.reconcile ==True:
                        if i.account_id.internal_type in ['payable' ,'receivable']:
                            print("i.partner_id.name",i.balance)
                            total=total+i.balance
        self.due_amount = total



class PurchaseOrder(models.Model):
    _inherit= 'purchase.order'
    _description = 'Purchase Order'


    due_amount= fields.Float('Due amount',compute="default_payment_method_id")

    @api.depends("partner_id")
    def default_payment_method_id(self):
        date = fields.Date.today()
        self.due_amount=0
        total = 0
        obj = self.env['account.move.line'].search([('partner_id', '=', self.partner_id.id),('date', '=', date)])
        for i in obj:
            if i.move_id.state =="posted":
                if i.reconciled==False and i.balance !=0:
                    if i.account_id.reconcile ==True:
                        if i.account_id.internal_type in ['payable' ,'receivable']:
                            print("i.partner_id.name",i.balance)
                            total=total+i.balance
        self.due_amount = total
