# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

from odoo import models

class Alumno(models.Model):
    _name = 'libros.alumno'
    _inherit='libros.usuario'
    
    dni=fields.String(String="DNI")
    lastAccess=fields.Date(String="Last access", default=fields.Date.today)