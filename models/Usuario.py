# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

from odoo import models

class Usuario(models.Model):
    _name = 'libros.usuario'
    _inherit = 'res.users'
    
    login = fields.String(String="Login", required=True)
    email = fields.String(String="Email", required=True)
    fullname = fields.String(String="Nombre completo", required=True)
    status = fields.Selection(
                              selection=[('1', 'ENABLED'),
                              ('2', 'DISABLED')], 
                              string="Estado del usuario", 
                              required=True)
    privilege = fields.Selection(
                                 selection=[('1', 'USER'),
                                 ('2', 'ADMIN')], 
                                 string="Privilegio del usuario", 
                                 required=True)
    password = fields.String(String="Contraseña", required=True)
    lastAccess = fields.DateTime(String="Último acceso", default=fields.DateTime.now, required=True)
    lastPasswordChange = fields.DateTime(String="Último cambio de contraseña", default=fields.DateTime.now, required=True)
    tipoUsuario = fields.Selection(
                                   selection=[('1', 'BIBLIOTECARIO'),
                                   ('2', 'PROFESOR')
                                   ('3', 'ALUMNO')], 
                                   string="Tipo de usuario", 
                                   required=True)