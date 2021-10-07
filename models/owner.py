# -*- coding: utf-8 -*-
from odoo import api, fields, models


class Owner(models.Model):
    _inherit = 'res.partner'

    name = fields.Char('Owner Name', required=True)
    pet = fields.Many2one('mp.pet', string= 'Thu cung')
    channel_ids = fields.Many2many('mail.channel', 'mail_channel_profile_partner',
                                   'partner_id', 'channel_id', copy=False)

