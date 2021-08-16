# -*- coding: utf-8 -*-
from odoo import api, fields, models, tools, _
from odoo.exceptions import UserError, ValidationError

class MyPet(models.Model):
    _name = "my.pet"
    _description = "My pet model"

    name = fields.Char('Pet Name', required=True)
    nickname = fields.Char('Nickname')
    description = fields.Text('Pet Description')
    age = fields.Integer('Pet Age', default=1)
    weight = fields.Float('Weight (kg)')
    #---------------------------------------------------------------------------------------
    dob = fields.Date('DOB', required=False)
    @api.depends('date_of_birth')
    def _compute_person_age(self):
        if self.date_of_birth:
            birth_date = datetime.strptime(self.birth_date, '%m/%d/%Y')
            self.age = (datetime.today() - birth_date).days / 365
    #---------------------------------------------------------------------------------------
    gender = fields.Selection([
        ('male', 'Male'),
        ('female', 'Female')
    ], string='Gender', default='male')
    species = fields.Many2one(comodel_name'', string='Species')
    hobbies = fields.Many2many(comodel_name='', string='Hobbies')
    pet_image = fields.Binary("Pet Image", attachment=True, help="Pet Image")    
    owner_id = fields.Many2one('res.partner', string='Owner')
    product_ids = fields.Many2many(comodel_name='product.product', 
                                string="Related Products", 
                                relation='pet_product_rel',
                                column1='col_pet_id',
                                column2='col_product_id')

#class SaleOrderLine(models.Model):
#    _inherit = 'sale.order.line'
#     x_field = fields.Char('X Field')

class MyPetSpecies(models.Model):
    _name
    
    