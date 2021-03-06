# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

# author Jonathan Vinan

from odoo import fields
from odoo import models
from odoo import api


class Grupo(models.Model):
    _name = 'libros.grupo'
    
    
    descripcion = fields.Text()
    nombre = fields.Char(string="Nombre", required=True)
    num_alumno = fields.Integer(string="Numero de Alumnos")
    
    #Relacion N:1 con profesor
    profesor_id = fields.Many2one('res.user', ondelete='cascade',
                                  string="Profesor",
                                  domain=[('profesor','=',True)])
    #Relacion N:1 con GrupoLibro
    grupo_libro_id = fields.One2many('libros.grupo_libro', 'grupo_id', 
                                     string="IdGrupo")
    #Relacion M:N con alumno
    alumno_id = fields.Many2many('res.user', string="Alumno")
    
    
    