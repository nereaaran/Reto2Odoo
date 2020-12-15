# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.


from odoo import models, fields

class GrupoLibro(models.Model):
    _name = 'libros.grupo_libro'
    
    fechaInicio = fields.Data(default=fields.Date.today, String="Fecha inicio")
    fechaFin = feilds.Data(String="Fecha fin")
    
    #Relacion 1:N con grupo
    grupo_id = fields.Many2one('libros.grupo', 'grupoLibro_id', ondelete='cascade', String="IdGrupo")
    #Relacion 1:N con libro
    libro_id = fields.Many2one('libros.libro', 'grupo_id', ondelte='cascade', String="Libro")
    #Relacion M:N con alumno
    alumno_id = fields.Many2many('res.user', String="Alumno") 
    