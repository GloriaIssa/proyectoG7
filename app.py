import functools
import os
from re import X

from flask import Flask, render_template, flash, current_app
from flask import redirect, request, url_for, session, g
from flask.templating import render_template_string
from datetime import datetime

import utils
from db import get_db, close_db
from werkzeug.security import generate_password_hash, check_password_hash

from config import dev
import forms

app = Flask(__name__)
app.config.from_object(dev)
app.secret_key = os.urandom(24)

opciones = {
    1: "Editar/Crear proveedores",
    2: "Consultar Proveedores",
    3: "Eliminar Proveedores"}

usuarios = ("SUPERADMIN", "ADMIN", "USER")

Lista_productos = {
    1001: "BMWi3",
    2001: "KIA NEW SPORTAGE 2.0",
    3001: "FORD EXPLORER LIMITED 3.5",
    4001: "Audi A5 Sportbag",
    5001: "Mercedes Benz E200"}

Lista_proveedor = ["BMW", "Audi", "Subaru", "Kia", "FORD", "Mercedes Benz"]

sesion_iniciada = False
usuario = None


@app.route("/", methods=["GET", "POST"])
@app.route("/inicio", methods=["GET", "POST"])
def inicio():
    if g.user:  # si ya inicio sesion
        # chequear el perfil
        # segun el perfil lo envia a la pagina segun Mapa de Navegabilidad
        return render_template('home.html', sesion_iniciada=sesion_iniciada, usuario=g.user)

    return render_template('index.html', sesion_iniciada=sesion_iniciada, usuario=g.user)


@app.route("/login", methods=["GET", "POST"])
def login():
    global sesion_iniciada, usuario
    login_form = forms.LoginForm(request.form)

    try:
        if g.user:
            return redirect(url_for('inicio'))

        if request.method == 'POST':
            db = get_db()
            error = None
            username = request.form['usuario']
            password = request.form['password']
            passhasheado = generate_password_hash(password)
            if not username:
                error = 'Debes ingresar el usuario'
                flash(error)
                return render_template('login.html')

            if not password:
                error = 'Contraseña requerida'
                flash(error)
                return render_template('login.html')

            user = db.execute(
                'SELECT * FROM usuarios WHERE codigo_usuario = ? AND password = ?', (
                    username, password)
            ).fetchone()
            if user is None:
                user = db.execute(
                    "SELECT * FROM usuarios WHERE codigo_usuario = ?", (username,)
                ).fetchone()
                if user is None:
                    error = 'Usuario no existe'
                else:
                    # Validar contraseña hash
                    # campo password de la tabla usuarios
                    store_password = user[7]
                    result = check_password_hash(store_password, password)
                    if result is False:
                        error = 'Contraseña inválida'
                    else:
                        session.clear()
                        # campo codigo_usuario de la tabla usuarios
                        session['user_id'] = user[1]
                        sesion_iniciada = True
                        usuario = session['user_id']
                        return redirect(url_for('inicio'))
                flash(error)
            else:
                session.clear()
                # campo codigo_usuario de la tabla usuarios
                session['user_id'] = user[1]
                if usuario == "SUPERADMIN":
                    return "Pagina de Super Administrador"
                elif usuario == "ADMIN":
                    return render_template("home.html")
                elif usuario == "USER":
                    return redirect(url_for('inicio'))
            flash(error)
            close_db()
        return render_template("login.html", form=login_form)
    except Exception as e:
        print(e)
        return render_template("login.html", form=login_form)


@app.route("/salir", methods=["POST"])
def salir():
    global sesion_iniciada
    sesion_iniciada = False
    g.user = None
    session.clear()
    return redirect(url_for('inicio'))


@app.route("/cancelar", methods=["POST"])
def cancelar():
    global sesion_iniciada
    sesion_iniciada = False
    return redirect(url_for('inicio'))


@app.route("/dashboard", methods=["GET", "POST"])
def dashboard():
    # si ya inicio sesion
    # chequear el perfil
    # segun el perfil mostrar informacion de acuerdo a él.
    return "Dashboard con Informacion del Inventario de Autos segun Perfil"
    # render_template('index.html')


@app.route("/admin", methods=["GET", "POST"])
def admin():
    # si ya inicio sesion
    # chequear el perfil
    return render_template('admin.html')
    # "Administracion de Usuarios"


@app.route("/registro", methods=["GET", "POST"])
def registro():
    # si ya inicio sesion
    # chequear el perfil
    return render_template('registro_user.html')
    # "Administracion de Usuarios"


@app.route('/articulos')
def articulos():
    if g.user:
        sql = "Select * fom productos"
        db = get_db()
        cursor = db.cursor()
        cursor.execute(sql)
        articulos = cursor.fetchall()
        close_db()
        return render_template_string("articulos.html", articulos=articulos)
    else:
        return redirect('login')


@app.route("/productos/<id_productos>", methods=["GET", "POST"])
def productos(id_productos):
    # LogicaAlgoritm Sprint 3

    try:
        id_productos = int(id_productos)
    except Exception as e:
        opcion = 0

    if id_productos in Lista_productos:
        return Lista_productos[id_productos]
    else:
        return f"Error producto :{id_productos} no existe"


@app.route("/productos/<opcion>", methods=["GET", "POST"])
def gestion_productos(opcion):
    # si ya inicio sesion
    # chequear el perfil
    opcion = int(opcion)
    if opcion == 1:
        return "Opcion 1 Editar/Crear Productos"
    else:
        return "Opcion 2 Consultar Productos"
    # Editar / Crear Productos
    # render_template('gproductos.html')


@app.route("/proveedores/<id_proveedor>", methods=["GET", "POST"])
def proveedores(id_proveedor):
    # LogicaAlgoritm Sprint 3
    if id_proveedor in Lista_proveedor:
        # si ya inicio sesion
        # chequear el perfil
        return f"Pagina de Gestion de Proveedores : {id_proveedor}"
    else:
        return f"Error proveedor :{id_proveedor} no existe"
    # Editar / Crear Proveedores
    # render_template('proveedor.html')


@app.route("/proveedor/<opcion>", methods=["GET", "POST"])
def gestion_proveedores(opcion):
    # return  "Opcion 1 Editar/Crear Proveedor"
    # si ya inicio sesion
    # chequear el perfil

    # LogicaAlgoritm Sprint3
    try:
        opcion = int(opcion)
    except Exception as e:
        opcion = 0

    if opcion in opciones:
        return opciones[opcion]
    else:
        return "Opcion Invalida"
    # Editar / Crear Proveedores
    # render_template('gproveedor.html')"""


@app.route('/reg_fabricante', methods=('GET', 'POST'))
def reg_fabricante():
    if g.user == None:
        return redirect(url_for('/login'))

    reg_fab_form = forms.FabricanteForm(request.form)
    try:
        if request.method == 'POST':
            cod_fab = request.form['cod_fab']
            tid_fab = request.form['tipoid_fab']
            nid_fab = request.form['nroid_fab']
            dv_fab = request.form['dv_nroid_fab']
            rsocial = request.form['rsocial_fab']
            nrep_fab = request.form['name_rep_fab']
            ncon_fab = request.form['name_con_fab']
            email = request.form['email_fab']
            cpais = request.form['codigo_pais']
            ciu_fab = request.form['ciudad']
            dir_fab = request.form['direccion']
            tel_fab = request.form['telefono']
            cel_fab = request.form['celular']
            cusuario = usuario
            error = None
            db = get_db()

            if not utils.isNroidValid(nid_fab):
                error = "El Nro. de ID del Fabricante debe ser numerico."
                print(error)
                return render_template('reg_fab.html', form=reg_fab_form)

            if not utils.isUsernameValid(rsocial):
                error = "El nombre del Fabricante debe ser alfanumerico o incluir solo '.','_','-'"
                print(error)
                return render_template('reg_fab.html', form=reg_fab_form)

            if not utils.isEmailValid(email):
                error = 'Correo invalido'
                print(error)
                return render_template('reg_fab.html', form=reg_fab_form)

            if db.execute('SELECT id_fabricante FROM fabricante WHERE nroid_fabricante = ?', (nid_fab,)).fetchone() is not None:
                error = 'Existe un Fabricante con ese Nro. de ID'.format(
                    nid_fab)
                print(error)
                return render_template('reg_fab.html', form=reg_fab_form)

            db.execute(
                '''INSERT INTO fabricante (cod_fabricante, tipoid_fabricante, nroid_fabricante, dv_nroid, razon_social_fabricante, nombre_representante,
                nombre_contacto, email_fabricante, codigo_pais, ciudad, direccion, telefono, celular, codigo_usuario) VALUES 
                (?,?,?,?,?,?,?,?,?,?,?,?,?,?)''',
                (cod_fab, tid_fab, nid_fab, dv_fab, rsocial, nrep_fab, ncon_fab,
                 email, cpais, ciu_fab, dir_fab, tel_fab, cel_fab, cusuario)
            )
            db.commit()
            close_db()

            print('Fabricante Registrado correctamente')
            return redirect('inicio')

        return render_template('reg_fab.html', form=reg_fab_form)
    except:
        print('ERROR- REG FABRICANTE')
        return render_template('reg_fab.html', form=reg_fab_form)


@app.route( '/reg_proveedor', methods=('GET', 'POST') )
def reg_proveedor():
    if g.user==None:
        return redirect( url_for( '/login' ) )
    
    reg_prov_form = forms.ProveedoresForm(request.form)
    try:
        if request.method == 'POST':
            cod_prov = request.form['cod_prov'] 
            tipoid_prov = request.form['tipoid_prov']
            nroid_prov  = request.form['nroid_prov']
            dv_nroid_prov = request.form['dv_nroid_prov'] 
            rsocial_prov = request.form['rsocial_prov']
            name_rep_prov = request.form['name_rep_prov']
            name_con_prov = request.form['name_con_prov']
            email_prov = request.form['email_prov']
            codigo_pais = request.form['codigo_pais']
            ciudad = request.form['ciudad']
            direccion = request.form['direccion']
            telefono = request.form['telefono']
            celular = request.form['celular'] 
            est_aut = request.form['est_aut']
            fec_sist = request.form['fec_sist']
            cod_user = request.form['cod_user']
            cusuario = usuario
            error = None
            db = get_db()

            if not utils.isNroidValid( nroid_prov ):
                error = "El Nro. de ID del Fabricante debe ser numerico."
                print( error )
                return render_template( 'reg_proveed.html', form = reg_prov_form )

            if not utils.isUsernameValid( rsocial_prov ):
                error = "El nombre del Fabricante debe ser alfanumerico o incluir solo '.','_','-'"
                print( error )
                return render_template( 'reg_proveed.html', form = reg_prov_form )

            if not utils.isEmailValid( email_prov ):
                error = 'Correo invalido'
                print( error )
                return render_template( 'reg_proveed.html', form = reg_prov_form )

            if db.execute( 'SELECT nroid_proveedor FROM proveedor WHERE nroid_prov = ?', (nroid_prov,) ).fetchone() is not None:
                error = 'Existe un Fabricante con ese Nro. de ID'.format( nroid_prov )
                print( error )
                return render_template( 'reg_proveed.html', form = reg_prov_form )

            db.execute(
                '''INSERT INTO proveedor (codigo_proveedor, tipoid_proveedor, nroid_proveedor, dv_nroid, razon_social_proveedor, nombre_representante,
                nombre_contacto, email_proveedor, codigo_pais, ciudad, direccion, telefono, celular, estado, fecha_sistema, codigo_usuario) VALUES 
                (?,?,?,?,?,?,?,?,?,?,?,?,?,?)''',
                (cod_prov, tipoid_prov, nroid_prov, dv_nroid_prov, rsocial_prov, name_rep_prov, name_con_prov, email_prov, codigo_pais, ciudad, direccion, telefono, celular, est_aut, fec_sist, cod_user, cusuario)
            )
            db.commit()
            close_db()

            print( 'Proveedor Registrado correctamente' )
            return redirect( 'inicio' )
        
        return render_template( 'reg_proveed.html', form = reg_prov_form )
    except:
        print('ERROR - REGISTRO DE PROVEEDORES')
        return render_template( 'reg_proveed.html', form = reg_prov_form )


@app.route("/ayuda", methods=["GET"])
def ayuda():
    # si ya inicio sesion
    # chequear el perfil
    return render_template('config.html')
    # Ayuda en General con aceso a Videos.
    # render_template('ayuda.html')


@app.before_request  # Decorador
def load_logged_in_user():
    user_id = session.get('user_id')

    if user_id is None:
        g.user = None
    else:
        g.user = get_db().execute(
            'SELECT * FROM usuarios WHERE codigo_usuario = ?', (user_id,)
        ).fetchone()


@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('inicio'))


@app.errorhandler(404)
def page_not_found(error):
    return "Pagina No Encontrada ... ", 404


if __name__ == '__main__':  # Cuando este corriendo de modo principal debe subir el servidor
    app.run()  # app.run(debug=True)     #Para que cuando haga un cambio y guarde el servidor se actualiza enseguida
