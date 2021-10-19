#from wtforms import Form
from flask_wtf import FlaskForm
from wtforms import IntegerField, StringField, PasswordField, SubmitField
from wtforms import TextField, TextAreaField, SelectField
from wtforms.fields.html5 import EmailField
from wtforms.fields import FileField
from wtforms.validators import Required, Email, Length

class LoginForm(FlaskForm):
    usuario = StringField('Usuario', validators=[Required(message='No dejar vacío, completar')])
    password = PasswordField('Password', validators=[Required(message='No dejar vacío, completar')])

class Contactenos(FlaskForm):
    nombre = StringField('Nombre', validators=[Required(message='No dejar vacío, completar')])
    correo = EmailField('Correo', validators=[Required(message='No dejar vacío, completar')])
    mensaje = StringField('Mensaje', validators=[Required(message='No dejar vacío, completar')])
    enviar = SubmitField('Enviar Mensaje')

class RegistroUsuario(FlaskForm):
    cod_usuario = StringField('Codigo Usuario', validators=[Required(message='No dejar vacío, completar'), Length(max=15)])
    nombre_usuario = StringField('Nombre Usuario', validators=[Required(message='No dejar vacío, completar'), Length(max=255)])
    email_usuario = EmailField('Email Usuario', validators=[Required(message='No dejar vacío, completar'), Email()])
    cargo = StringField('Cargo Usuario', validators=[Required(message='No dejar vacío, completar'), Length(max=15)])
    foto = FileField('Selecciona imagen:')
    codigo_rol = SelectField('Rol de Usuario', choices=[("SUPERADMIN"), ("ADMIN"), ("USUARIO")])
    password = PasswordField('Contraseña', validators=[Required(message='No dejar vacío, completar'), Length(max=50)])
    codigo_pais = StringField('Pais', validators=[Required(message='No dejar vacío, completar')])
    direccion = TextField('Direccion', validators=[Required(message='No dejar vacío, completar'), Length(max=255)])    
    telefono = StringField('Telefono', validators=[Required(message='No dejar vacío, completar'), Length(max=50)])
    celular = StringField('celular', validators=[Required(message='No dejar vacío, completar'), Length(max=50)])
    ciudad = StringField('ciudad', validators=[Required(message='No dejar vacío, completar'), Length(max=50)])
    submit = SubmitField('Registrar Usuario')