from wtforms import Form
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.fields.html5 import EmailField
from wtforms.validators import DataRequired

class LoginForm(Form):
    usuario = StringField('Usuario', validators=[DataRequired(message='No dejar vacío, completar')])
    password = PasswordField('Password', validators=[DataRequired(message='No dejar vacío, completar')])

class Contactenos(Form):
    nombre = StringField('Nombre', validators=[DataRequired(message='No dejar vacío, completar')])
    correo = EmailField('Correo', validators=[DataRequired(message='No dejar vacío, completar')])
    mensaje = StringField('Mensaje', validators=[DataRequired(message='No dejar vacío, completar')])
    enviar = SubmitField('Enviar Mensaje')

