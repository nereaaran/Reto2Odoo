# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

# author Cristina Milea

from odoo import api
from odoo import fields
from odoo import models
from odoo import api
from odoo import exceptions

class Alumno(models.Model):
    _inherit = 'res.users'
    
    dni = fields.Char(string="DNI", required=True, size=9)
    fechaNacimiento = fields.Date(string="Fecha de nacimiento", required=True)
    
    #Relacion N:M con grupo.
    grupo_id = fields.Many2many('libros.grupo', string="Grupo")
    #Relacion 1:N con alumno_libro
    libro_id = fields.One2many('libros.alumno_libro', 'alumno_id', string="Libro")
    
    # Que la fecha de nacimiento sea menor a la de hoy
    @api.constrains('fechaNacimiento')
    def _check_fecha_nacimiento(self):
        date_today = fields.Date.today()
        for r in self:
            if r.fechaNacimiento >= date_today:
                 raise exceptions.ValidationError("Fecha de nacimiento must be before today")

    
    
