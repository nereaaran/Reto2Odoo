# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

from odoo import models

class Usuario(models.Model):
    _name = 'libros.usuario'
    _inherit='res.users'
    
    idUsuario
    login=fields.String(String="Login", required=True)
    email=fields.String(String="Email", required=True)
    fullname=fields.String(String="Full Name", required=True)
    class Status(Enum):
        ENABLED
        DISABLED
    class Privilege(Enum):
        USER
        ADMIN
    password=fields.String(String="Password", required=True)
    lastAccess=fields.Date(String="Last access", default=fields.Date.today, required=True)
    lastPasswordChange=fields.Date(String="Last password change", default=fields.Date.today, required=True)
    class TipoUsuario(Enum):
        BIBLIOTECARIO
        PROFESOR
        ALUMNO