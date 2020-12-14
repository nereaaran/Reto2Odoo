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
    profesores_ids = fields.Many2one('res.user', 'grupo_ids', ondelete='set null', String = "Profesor")
    #Relacion N:1 con GrupoLibro
    grupolibro = fields.One2many('libros.grupo_libro', 'grupos', ondete='cascade')
