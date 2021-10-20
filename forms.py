#from wtforms import Form
from flask_wtf import FlaskForm
from wtforms import IntegerField, StringField, PasswordField, SubmitField
from wtforms import TextField, TextAreaField, SelectField
from wtforms.fields.html5 import EmailField
from wtforms.fields import FileField
from wtforms.validators import DataRequired, Email, Length

class LoginForm(FlaskForm):
    usuario = StringField('Usuario', validators=[DataRequired(message='No dejar vacío, completar')])
    password = PasswordField('Password', validators=[DataRequired(message='No dejar vacío, completar')])

class Contactenos(FlaskForm):
    nombre = StringField('Nombre', validators=[DataRequired(message='No dejar vacío, completar')])
    correo = EmailField('Correo', validators=[DataRequired(message='No dejar vacío, completar')])
    mensaje = StringField('Mensaje', validators=[DataRequired(message='No dejar vacío, completar')])
    enviar = SubmitField('Enviar Mensaje')

class RegistroUsuario(FlaskForm):
    cod_usuario = StringField('Codigo Usuario', validators=[DataRequired(message='No dejar vacío, completar'), Length(max=15)])
    nombre_usuario = StringField('Nombre Usuario', validators=[DataRequired(message='No dejar vacío, completar'), Length(max=255)])
    email_usuario = EmailField('Email Usuario', validators=[DataRequired(message='No dejar vacío, completar'), Email()])
    cargo = StringField('Cargo Usuario', validators=[DataRequired(message='No dejar vacío, completar'), Length(max=15)])
    foto = FileField('Selecciona imagen:')
    codigo_rol = SelectField('Rol de Usuario', choices=[("SUPERADMIN"), ("ADMIN"), ("USUARIO")])
    password = PasswordField('Contraseña', validators=[DataRequired(message='No dejar vacío, completar'), Length(max=50)])
    codigo_pais = StringField('Pais', validators=[DataRequired(message='No dejar vacío, completar')])
    direccion = TextField('Direccion', validators=[DataRequired(message='No dejar vacío, completar'), Length(max=255)])    
    telefono = StringField('Telefono', validators=[DataRequired(message='No dejar vacío, completar'), Length(max=50)])
    celular = StringField('celular', validators=[DataRequired(message='No dejar vacío, completar'), Length(max=50)])
    ciudad = StringField('ciudad', validators=[DataRequired(message='No dejar vacío, completar'), Length(max=50)])
    submit = SubmitField('Registrar Usuario')

class FabricanteForm(FlaskForm):
    cod_fab = StringField('Codigo Fabricante', validators=[DataRequired(message='No dejar vacío, completar'), Length(max=15)])
    tipoid_fab = SelectField('Tipo ID', choices=[("CC"), ("NUIP"), ("CE"), ("NIT")])
    nroid_fab = StringField('Nro. ID', validators=[DataRequired(message='')])    
    dv_nroid_fab = StringField('DV', validators=[DataRequired(message='')])
    rsocial_fab = StringField('Razon Social', validators=[DataRequired(message='No dejar vacío, completar'), Length(max=255)])
    name_rep_fab = StringField('Nombre Representante', validators=[DataRequired(message='No dejar vacío, completar'), Length(max=255)])
    name_con_fab = StringField('Nombre Contacto', validators=[DataRequired(message='No dejar vacío, completar'), Length(max=255)])
    email_fab = EmailField('Email Fabricante', validators=[DataRequired(message='No dejar vacío, completar'), Email()])
    codigo_pais = StringField('Pais', validators=[DataRequired(message='No dejar vacío, completar')])
    ciudad = StringField('Ciudad', validators=[DataRequired(message='No dejar vacío, completar')])    
    direccion = TextField('Direccion', validators=[DataRequired(message='No dejar vacío, completar'), Length(max=255)])    
    telefono = StringField('Telefono', validators=[DataRequired(message='No dejar vacío, completar'), Length(max=50)])
    celular = StringField('celular', validators=[DataRequired(message='No dejar vacío, completar'), Length(max=50)])
    submit = SubmitField('Registrar Usuario')