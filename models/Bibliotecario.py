# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

from odoo import api
from odoo import fields
from odoo import models

class Bibliotecario(models.Model):
    _inherit = 'libros.usuario'
    
    libro_id = fields.One2many('libros.libro', 'usuario_id', string="Libro")
