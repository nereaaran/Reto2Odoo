# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.


from odoo import models, fields

class GrupoLibro(models.Model):
    _name = 'libros.grupo_libro'
    
    fechaInicio = fields.Data(default=fields.Date.today, String="Fecha inicio")
    fechaFin = feilds.Data(String="Fecha fin")
    
    #Relacion 1:N con grupo
    grupos = fields.Many2one('libros.grupo', 'grupolibro', ondelete='cascade', String="GrupoId")
    #Relacion 1:N con libro
    libros = fields.Many2one('libros.libro', 'nombreRelacion', ondelte='cascade', String="LibroId")
    
    