# -*- coding: utf-8 -*-
from odoo import models, fields, api

class CrmTagInherit(models.Model):
    _inherit = 'crm.tag'

    company_id = fields.Many2one('res.company', string='Company', 
                                default=lambda self: self.env.company)
    tag_type = fields.Selection([
        ('customer', 'Customer'),
        ('vendor', 'Vendor'),
        ('product', 'Product'),
        ('account', 'Account')
    ], string='Tag Type')
    tag_type_id = fields.Many2one('crm.tag.type', string='Tag Type')
    customer_count = fields.Integer(compute='_compute_counts')
    vendor_count = fields.Integer(compute='_compute_counts')
    product_count = fields.Integer(compute='_compute_counts')
    account_count = fields.Integer(compute='_compute_counts')

    @api.depends('tag_type')
    def _compute_counts(self):
        for tag in self:
            if tag.tag_type == 'customer':
                tag.customer_count = self.env['res.partner'].search_count([
                    ('company_tag', '=', tag.id),
                    ('supplier_rank', '=', 0),
                    '|', ('company_id', '=', False), ('company_id', '=', tag.company_id.id)
                ])
                tag.vendor_count = 0
                tag.product_count = 0
                tag.account_count = 0
            elif tag.tag_type == 'vendor':
                tag.vendor_count = self.env['res.partner'].search_count([
                    ('company_tag', '=', tag.id),
                    ('supplier_rank', '>', 0),
                    '|', ('company_id', '=', False), ('company_id', '=', tag.company_id.id)
                ])
                tag.customer_count = 0
                tag.product_count = 0
                tag.account_count = 0
            elif tag.tag_type == 'product':
                tag.product_count = self.env['product.template'].search_count([
                    ('company_tag', '=', tag.id),
                    '|', ('company_id', '=', False), ('company_id', '=', tag.company_id.id)
                ])
                tag.customer_count = 0
                tag.vendor_count = 0
                tag.account_count = 0
            elif tag.tag_type == 'account':
                tag.account_count = self.env['account.account.tag'].search_count([
                    ('crm_tag_id', '=', tag.id),
                    '|', ('company_id', '=', False), ('company_id', '=', tag.company_id.id)
                ])
                tag.customer_count = 0
                tag.vendor_count = 0
                tag.product_count = 0
            else:
                tag.customer_count = 0
                tag.vendor_count = 0
                tag.product_count = 0
                tag.account_count = 0

    def action_view_customers(self):
        return {
            'name': 'Customers',
            'type': 'ir.actions.act_window',
            'res_model': 'res.partner',
            'view_mode': 'tree,form',
            'domain': [
                ('company_tag', '=', self.id), 
                ('supplier_rank', '=', 0),
                '|', ('company_id', '=', False), ('company_id', '=', self.company_id.id)
            ],
        }

    def action_view_vendors(self):
        return {
            'name': 'Vendors',
            'type': 'ir.actions.act_window',
            'res_model': 'res.partner',
            'view_mode': 'tree,form',
            'domain': [
                ('company_tag', '=', self.id), 
                ('supplier_rank', '>', 0),
                '|', ('company_id', '=', False), ('company_id', '=', self.company_id.id)
            ],
        }

    def action_view_products(self):
        return {
            'name': 'Products',
            'type': 'ir.actions.act_window',
            'res_model': 'product.template',
            'view_mode': 'tree,form',
            'domain': [
                ('company_tag', '=', self.id),
                '|', ('company_id', '=', False), ('company_id', '=', self.company_id.id)
            ],
        }

    def action_view_accounts(self):
        return {
            'name': 'Account Tags',
            'type': 'ir.actions.act_window',
            'res_model': 'account.account.tag',
            'view_mode': 'tree,form',
            'domain': [
                ('crm_tag_id', '=', self.id),
                '|', ('company_id', '=', False), ('company_id', '=', self.company_id.id)
            ],
        }

class ResPartnerInherit(models.Model):
    _inherit = 'res.partner'

    company_tag = fields.Many2one('crm.tag', string='Company Tag', 
                                 domain="[('tag_type', 'in', ['customer', 'vendor']), '|', ('company_id', '=', False), ('company_id', '=', company_id)]")
    has_my_customer_tag = fields.Boolean(compute='_compute_has_my_tags', search='_search_has_my_customer_tag')
    has_my_vendor_tag = fields.Boolean(compute='_compute_has_my_tags', search='_search_has_my_vendor_tag')

    @api.depends('company_tag')
    def _compute_has_my_tags(self):
        for record in self:
            record.has_my_customer_tag = record.company_tag.id in self.env.user.allowed_customer_tags.ids
            record.has_my_vendor_tag = record.company_tag.id in self.env.user.allowed_vendor_tags.ids

    def _search_has_my_customer_tag(self, operator, value):
        if operator == '=' and value:
            return ['&', ('company_id', 'in', [False] + self.env.user.company_ids.ids), 
                    ('company_tag', 'in', self.env.user.allowed_customer_tags.ids)]
        return ['|', ('company_id', 'not in', self.env.user.company_ids.ids), 
                ('company_tag', 'not in', self.env.user.allowed_customer_tags.ids)]

    def _search_has_my_vendor_tag(self, operator, value):
        if operator == '=' and value:
            return ['&', ('company_id', 'in', [False] + self.env.user.company_ids.ids), 
                    ('company_tag', 'in', self.env.user.allowed_vendor_tags.ids)]
        return ['|', ('company_id', 'not in', self.env.user.company_ids.ids), 
                ('company_tag', 'not in', self.env.user.allowed_vendor_tags.ids)]

class ResUsersInherit(models.Model):
    _inherit = 'res.users'

    allowed_customer_tags = fields.Many2many(
        'crm.tag',
        'res_users_customer_tag_rel',
        'user_id', 'tag_id',
        string='Allowed Customer Tags',
        domain="[('tag_type', '=', 'customer'), '|', ('company_id', '=', False), ('company_id', 'in', company_ids)]"
    )
    allowed_vendor_tags = fields.Many2many(
        'crm.tag',
        'res_users_vendor_tag_rel',
        'user_id', 'tag_id',
        string='Allowed Vendor Tags',
        domain="[('tag_type', '=', 'vendor'), '|', ('company_id', '=', False), ('company_id', 'in', company_ids)]"
    )
    allowed_product_tags = fields.Many2many(
        'crm.tag',
        'res_users_product_tag_rel',
        'user_id', 'tag_id',
        string='Allowed Product Tags',
        domain="[('tag_type', '=', 'product'), '|', ('company_id', '=', False), ('company_id', 'in', company_ids)]"
    )
    allowed_account_tags = fields.Many2many(
        'crm.tag',
        'res_users_account_tag_rel',
        'user_id', 'tag_id',
        string='Allowed Account Tags',
        domain="[('tag_type', '=', 'account'), '|', ('company_id', '=', False), ('company_id', 'in', company_ids)]"
    )

class ProductTemplateInherit(models.Model):
    _inherit = 'product.template'

    company_tag = fields.Many2one('crm.tag', string='Company Tag', 
                                 domain="[('tag_type', '=', 'product'), '|', ('company_id', '=', False), ('company_id', '=', company_id)]")
    has_my_product_tag = fields.Boolean(compute='_compute_has_my_tag', search='_search_has_my_tag')

    @api.depends('company_tag')
    def _compute_has_my_tag(self):
        for record in self:
            record.has_my_product_tag = record.company_tag.id in self.env.user.allowed_product_tags.ids

    def _search_has_my_tag(self, operator, value):
        if operator == '=' and value:
            return ['&', ('company_id', 'in', [False] + self.env.user.company_ids.ids), 
                    ('company_tag', 'in', self.env.user.allowed_product_tags.ids)]
        return ['|', ('company_id', 'not in', self.env.user.company_ids.ids), 
                ('company_tag', 'not in', self.env.user.allowed_product_tags.ids)]

class ProductTag(models.Model):
    _inherit = 'product.tag'

    company_id = fields.Many2one('res.company', string='Company', 
                                default=lambda self: self.env.company)
    tag_type = fields.Selection(
        related='crm_tag_id.tag_type',
        string='Tag Type',
        readonly=False
    )
    crm_tag_id = fields.Many2one('crm.tag', string='CRM Tag', 
                                domain="[('tag_type', '=', 'product'), '|', ('company_id', '=', False), ('company_id', '=', company_id)]")
    is_allowed_tag = fields.Boolean(
        string='Is Allowed Tag',
        compute='_compute_is_allowed_tag',
        search='_search_is_allowed_tag'
    )

    @api.depends('crm_tag_id')
    def _compute_is_allowed_tag(self):
        for record in self:
            record.is_allowed_tag = record.crm_tag_id.id in self.env.user.allowed_product_tags.ids

    def _search_is_allowed_tag(self, operator, value):
        if operator == '=' and value:
            return ['&', ('company_id', 'in', [False] + self.env.user.company_ids.ids), 
                    ('crm_tag_id', 'in', self.env.user.allowed_product_tags.ids)]
        return ['|', ('company_id', 'not in', self.env.user.company_ids.ids), 
                ('crm_tag_id', 'not in', self.env.user.allowed_product_tags.ids)]

class AccountTagInherit(models.Model):
    _inherit = 'account.account.tag'

    company_id = fields.Many2one('res.company', string='Company', 
                                default=lambda self: self.env.company)
    tag_type = fields.Selection([
        ('customer', 'Customer'),
        ('vendor', 'Vendor'),
        ('product', 'Product'),
        ('account', 'Account')
    ], string='Tag Type')
    crm_tag_id = fields.Many2one('crm.tag', string='CRM Tag', 
                                domain="[('tag_type', '=', 'account'), '|', ('company_id', '=', False), ('company_id', '=', company_id)]")
    is_allowed_tag = fields.Boolean(
        string='Is Allowed Tag',
        compute='_compute_is_allowed_tag',
        search='_search_is_allowed_tag'
    )
    account_count = fields.Integer(compute='_compute_account_count')

    @api.depends('crm_tag_id')
    def _compute_is_allowed_tag(self):
        for record in self:
            record.is_allowed_tag = record.crm_tag_id.id in self.env.user.allowed_account_tags.ids

    def _search_is_allowed_tag(self, operator, value):
        if operator == '=' and value:
            return ['&', ('company_id', 'in', [False] + self.env.user.company_ids.ids), 
                    ('crm_tag_id', 'in', self.env.user.allowed_account_tags.ids)]
        return ['|', ('company_id', 'not in', self.env.user.company_ids.ids), 
                ('crm_tag_id', 'not in', self.env.user.allowed_account_tags.ids)]
    
    @api.depends()
    def _compute_account_count(self):
        for tag in self:
            tag.account_count = self.env['account.account'].search_count([
                ('tag_ids', 'in', tag.id),
                '|', ('company_id', '=', False), ('company_id', '=', tag.company_id.id)
            ])
    
    def action_view_accounts(self):
        return {
            'name': 'Accounts',
            'type': 'ir.actions.act_window',
            'res_model': 'account.account',
            'view_mode': 'tree,form',
            'domain': [
                ('tag_ids', 'in', self.id),
                '|', ('company_id', '=', False), ('company_id', '=', self.company_id.id)
            ],
        }

class ResCompanyInherit(models.Model):
    _inherit = 'res.company'

    allowed_customer_tags = fields.Many2many(
        'crm.tag',
        'res_company_customer_tag_rel',
        'company_id', 'tag_id',
        string='Allowed Customer Tags',
        domain="[('tag_type', '=', 'customer')]"
    )
    allowed_vendor_tags = fields.Many2many(
        'crm.tag',
        'res_company_vendor_tag_rel',
        'company_id', 'tag_id',
        string='Allowed Vendor Tags',
        domain="[('tag_type', '=', 'vendor')]"
    )
    allowed_product_tags = fields.Many2many(
        'crm.tag',
        'res_company_product_tag_rel',
        'company_id', 'tag_id',
        string='Allowed Product Tags',
        domain="[('tag_type', '=', 'product')]"
    )
    allowed_account_tags = fields.Many2many(
        'crm.tag',
        'res_company_account_tag_rel',
        'company_id', 'tag_id',
        string='Allowed Account Tags',
        domain="[('tag_type', '=', 'account')]"
    )