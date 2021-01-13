# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

# author Cristina Milea

from odoo import api
from odoo import fields
from odoo import models

class Alumno(models.Model):
    _inherit = 'res.users'
    
    dni = fields.Char(string="DNI", required=True, size=9)
    fechaNacimiento = fields.Date(string="Fecha de nacimiento", required=True, domain=[('fechaNacimiento', '<', fields.Date.today())])
    
    #Relacion N:M con grupo.
    grupo_id = fields.Many2many('libros.grupo', string="Grupo")
    #Relacion 1:N con alumno_libro
    libro_id = fields.One2many('libros.alumno_libro', 'alumno_id', string="Libro")
    
    #@api.constrains('dni')
    #def _longitud_maxima_dni(self):
    #    if len(self.dni) > 9:
    #        return {
    #            'warning': {
    #                'title': "'dni' invalido",
    #                'message': "El DNI no puede tener mas de 9 caracteres",
    #                },
    #        }