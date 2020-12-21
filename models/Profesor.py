# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

from odoo import api
from odoo import fields
from odoo import models

class Profesor(models.Model):
    _inherit = 'res.users'
    
    telefono = fields.Integer(string="Telefono")
    
    #Relacion 1:N con grupo
    grupo_id = fields.One2many('libros.grupo', 'profesor_id', string ="Grupo")
