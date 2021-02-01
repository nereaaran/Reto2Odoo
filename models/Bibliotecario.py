# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

# author Cristina Milea

from odoo import fields
from odoo import models

class Bibliotecario(models.Model):
    _inherit = 'res.users'
    
    libro_id = fields.One2many('libros.libro', 'bibliotecario_id', string="Libro")