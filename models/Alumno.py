# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

# author Cristina Milea

from datetime import datetime
from odoo import api
from odoo import fields
from odoo import models

class Alumno(models.Model):
    _inherit = 'res.users'
    
    dni = fields.Char(string="DNI", required=True, size=9)
    fechaNacimiento = fields.Date(string="Fecha de nacimiento", required=True)
    
    #Relacion N:M con grupo.
    grupo_id = fields.Many2many('libros.grupo', string="Grupo")
    #Relacion 1:N con alumno_libro
    libro_id = fields.One2many('libros.alumno_libro', 'alumno_id', string="Libro")
    
    #@api.constrains('fechaNacimiento')
    #def _fecha_nacimiento_anterior_a_hoy(self):
    #    fechaDeNacimiento=datetime.datetime.strptime(self.fechaNacimiento, "%Y-%m-%d")
    #    if fechaDeNacimiento >= datetime.today():
    #        raise exceptions.ValidationError("La fecha de nacimiento tiene que ser anterior a la fecha actual")
