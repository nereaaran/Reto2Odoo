# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

from odoo import api
from odoo import fields
from odoo import models

class Alumno(models.Model):
    _inherit = 'res.users'
    
    dni = fields.Char(string="DNI")
    fechaNacimiento = fields.Date(string="Fecha de nacimiento")
    
    #Relacion N:M con grupo.
    grupo_id = fields.Many2many('libros.grupo', string="Grupo")
    #Relacion 1:N con alumno_libro
    libro_id = fields.One2many('libros.alumno_libro', 'alumno_id', string="Libro")