# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

# author Nerea Aranguren

from odoo import fields
from odoo import models

class Libro(models.Model):
    # Nombre del modulo en Odoo
    _name = 'libros.libro'
    
    # El titulo del libro.
    titulo = fields.Char(string="Titulo", required=True)
    # El autor del libro.
    autor = fields.Char(string="Autor", required=True)
    # La editorial del libro.
    editorial = fields.Char(string="Editorial", required=True)
    # El isbn del libro.
    isbn = fields.Integer(string="ISBN", required=True)
    # El genero literario del libro.
    genero = fields.Char(string="Genero literario", required=True)
    # La cantidad total que hay del libro.
    cantidadTotal = fields.Integer(string="Cantidad total", required=True)
    # La cantidad disponible que hay del libro.
    cantidadDisponible = fields.Integer(string="Cantidad disponible", required=True)
    # Variable que indica si el libro se puede descargar o no.
    descargable = fields.Boolean(string="Descargable", required=True)
    # Link de descarga del libro.
    linkDescarga = fields.Char(string="Link de descarga")
    
    # Referencia a la relacion 1:N con bibliotecario
    bibliotecario_id = fields.Many2one('libros.bibliotecario', string="Bibliotecario", ondelete='cascade')
    # Referencia a la relacion 1:N con la tabla relacional alumno libro.
    alumno_id = fields.One2many('libros.alumno_libro', 'libro_id', string="Alumno")
    # Referencia a la relacion 1:N con la tabla relacional grupo libro.
    grupo_id = fields.One2many('libros.grupo_libro', 'libro_id', string = "Grupo")