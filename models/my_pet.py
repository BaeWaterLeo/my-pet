# -*- coding: utf-8 -*-
from odoo import api, fields, models, tools, _
import datetime


class MyPet(models.Model):
    _name = "mp.pet"
    _description = "My pet model"

    name = fields.Char('Pet Name', required=True)
    nickname = fields.Char('Nickname')
    description = fields.Text('Pet Description')
    weight = fields.Float('Weight (kg)')
    pet_dob = fields.Date('DOB', required=True)
    pet_age = fields.Char('Pets Age', compute='_calculate_age')

    @api.depends('pet_dob')
    def _calculate_age(self):
        today_date = datetime.date.today()
        for pet in self:
            if pet.pet_dob:
                pet_dob = fields.Datetime.to_datetime(pet.pet_dob).date()
                total_age = str(int((today_date - pet_dob).days / 365))
                pet.pet_age = total_age
            else:
                pet.pet_age = "Wrong pet's birthday"

    gender = fields.Selection([
        ('male', 'Male'),
        ('female', 'Female')
    ], string='Gender', default='male')

    pet_image = fields.Binary("Pet Image", attachment=True, help="Pet Image")

    # owner_id = fields.Many2many(comodel_name="mp.pet", string="Pet's Owner",
    #                             relation='pet_owner_rel', readonly=True)


