# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

from odoo import models

class AlimnoLibro(models.Model):
    # Nombre del modulo en Odoo
    _name = 'libros.alumno_libro'
    
    # Fecha de asignacion
    fecha_asignado = fields.Date.today(string="Fecha Asignado", default = fields.Date.today())
    # Fecha limite
    fecha_limite = fields.Date.today(string="Fecha Limite")

    # Variable relacionada con la tabla alumno.
    alumno_id = fields.Many2one('libros.alumno', required = True, ondelete='cascade')
    # Variable relacionada con la tabla libro.
    libro_id = fields.Many2one('libros.libro', required = True, ondelete='cascade')
    
    