# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

# author Jonathan Vinan

from odoo import fields
from odoo import models

class Grupolibro(models.Model):
    _name = 'libros.grupo_libro'
    
    fecha_inicio = fields.Date(default=fields.Date.today)
    fecha_fin = fields.Date(string="Fecha fin")
    
    #Relacion 1:N con grupo
    grupo_id = fields.Many2one('libros.grupo', ondelete='cascade', string="IdGrupo")
    #Relacion 1:N con libro
    libro_id = fields.Many2one('libros.libro', ondelte='cascade', string="IdLibro")