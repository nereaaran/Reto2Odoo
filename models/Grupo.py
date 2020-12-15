# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

from odoo import models, fields

class Grupo(models.Model):
    _name = 'libros.grupo'
    
    descripcion = fields.Text()
    nombre = fields.Char(String="Nombre", required=True)
    numAlumno = fields.Integer(String="Numero de Alumnos")
    
    #Relacion N:1 con profesor
    profeso_id = fields.Many2one('res.user', ondelete='cascade',
                                String = "Profesor", requered=True)
    #Relacion N:1 con GrupoLibro
    grupoLibro_id = fields.One2many('libros.grupo_libro', 'grupo_id', 
                                String = "id_grupoLibro")
