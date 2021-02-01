# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

# author Cristina Milea

from odoo import api
from odoo import fields
from odoo import models
from odoo import exceptions

class Usuario(models.Model):
    _inherit = 'res.users'
    
    privilege = fields.Selection(
                                 selection=[('1', 'USER'),
                                 ('2', 'ADMIN')], 
                                 string="Privilegio del usuario",
                                 default='1',
                                 required=True)
    lastPasswordChange = fields.Datetime(string="Ultimo cambio del contrasenia", default=fields.Datetime.now, required=True)
    tipoUsuario = fields.Selection(
                                   selection=[('1', 'BIBLIOTECARIO'),
                                   ('2', 'PROFESOR'),
                                   ('3', 'ALUMNO')],
                                   string="Tipo de usuario",
                                   default='3',
                                   required=True)
                                   
    # Comprueba si el campo password esta informado.                             
    @api.constrains('password')
    def _check_passsword_has_text(self):
        if not self.password:
            raise exceptions.ValidationError("Password can't be empty")