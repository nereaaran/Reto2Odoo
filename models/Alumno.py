# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

from odoo import models

class Alumno(models.Model):
    _name = 'libros.alumno'
    _inherit = 'libros.usuario'
    
    dni = fields.String(String="DNI")
    fechaNacimiento = fields.Date(String="Fecha de nacimiento")
    
    #Relación N:M con grupo.
    grupo_id = fields.Many2Many('libros.grupo', String="Grupo")
    #Relación 1:N con alumno_libro
    libro_id=fields.One2Many('libros.alumno_libro', 'alumno_id', String="Libro")