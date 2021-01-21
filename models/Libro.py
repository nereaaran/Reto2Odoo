# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

# author Nerea Aranguren

from odoo import fields
from odoo import models
from odoo import api
from odoo import exceptions

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
    isbn = fields.Float(string="ISBN", size=13, digits=(13, 0), required=True)
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
    grupo_id = fields.One2many('libros.grupo_libro', 'libro_id', string="Grupo")
    
    
    # Avisa al usuario de que el isbn supera o esta debajo del valor permitido.
    @api.onchange('isbn')
    def _verify_isbn(self):
        if self.isbn > 9999999999999.0:
            return {
                'warning': {
                    'title': "Incorrect isbn value",
                    'message': "The isbn cant be over 13 digits",
                },
            }
        elif self.isbn < 0:
            return {
                'warning': {
                    'title': "Incorrect isbn value",
                    'message': "The isbn cant be negative",
                },
            }
            
    # Avisa al usuario de que la cantidad total no puede ser negativa.
    @api.onchange('cantidadTotal')
    def _verify_cantidad_total(self):
        if self.cantidadTotal < 0:
            return {
                'warning': {
                    'title': "Incorrect Cantidad Total value",
                    'message': "Cantidad Total cant be negative",
                },
            }
            
    # Avisa al usuario de que la cantidad disponible no puede ser negativa.
    @api.onchange('cantidadDisponible')
    def _verify_cantidad_disponible(self):
        if self.cantidadDisponible < 0:
            return {
                'warning': {
                    'title': "Incorrect Cantidad Disponible value",
                    'message': "Cantidad Disponible cant be negative",
                },
            }
            
    # Restringe salvar los datos si la cantidad disponible es mayor a la 
    # cantidad total.
    @api.constrains('cantidadTotal', 'cantidadDisponible')
    def _check_valid_cantidades(self):
        for r in self:
            if r.cantidadTotal < r.cantidadDisponible:
                raise exceptions.ValidationError("Cantidad Disponible cant be bigger than Cantidad Total")
          
    # Restringe salvar los datos si el isbn supera el valor permitido.
    @api.onchange('isbn')
    def _check_isbn(self):
        for r in self:
            if r.isbn > 9999999999999.0:
                raise exceptions.ValidationError("The isbn cant be negative over 13 digits")
            elif r.isbn < 0.0:
                raise exceptions.ValidationError("The isbn cant be negative")
             