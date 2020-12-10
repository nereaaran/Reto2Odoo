# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

from odoo import models

class Libro(models.Model):
    _name = 'libros.libro'
    idLibro = field.Integer(string="")