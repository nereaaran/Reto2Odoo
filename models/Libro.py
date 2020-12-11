# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

from odoo import models

class Libro(models.Model):
    _name = 'libros.libro'
    
    idLibro = fields.Integer(string = "Id Libro", required = True) ############### index
    titulo = fields.String(string = "Titulo", required = True)
    autor = fields.String(string = "Autor", required = True)
    editorial = fields.String(string = "Editorial", required = True)
    isbn = fields.Integer(string = "ISBN", required = True)
    genero = fields.String(string = "Genero literario", required = True)
    cantidadTotal = fields.Integer(string = "Cantidad total", required = True)
    cantidadDisponible = fields.Integer(string = "Cantidad disponible", required = True)
    descargable = fields.Boolean(string = "Descargable", required = True)
    linkDescarga = fields.String(string = "Link de descarga")
    
    
    