import functools
import os  
from re import X

from flask import Flask, render_template, flash, current_app
from flask import redirect, request, url_for, session, g
from flask.templating import render_template_string

import utils
from db import get_db, close_db
from werkzeug.security import generate_password_hash, check_password_hash

from config import dev
import forms

app=Flask(__name__)
app.config.from_object(dev)
app.secret_key = os.urandom(24)

opciones={
    1: "Editar/Crear proveedores",
    2: "Consultar Proveedores",
    3: "Eliminar Proveedores"}

usuarios=("SUPERADMIN", "ADMIN", "USER")

Lista_productos={
    1001: "BMWi3",
    2001: "KIA NEW SPORTAGE 2.0",
    3001: "FORD EXPLORER LIMITED 3.5",
    4001: "Audi A5 Sportbag",
    5001: "Mercedes Benz E200"}

Lista_proveedor=["BMW", "Audi", "Subaru", "Kia", "FORD", "Mercedes Benz"] 

sesion_iniciada=False
usuario=None

@app.route("/", methods=["GET"])
@app.route("/inicio", methods=["GET"])
def inicio():
    if g.user: # si ya inicio sesion 
       # chequear el perfil
       # segun el perfil lo envia a la pagina segun Mapa de Navegabilidad
       return render_template('index.html', sesion_iniciada=sesion_iniciada, usuario=g.user)

    return render_template('index.html', sesion_iniciada=sesion_iniciada, usuario=usuario)
    

@app.route("/login", methods=["GET", "POST"])
def login():
    global sesion_iniciada, usuario
    login_form = forms.LoginForm(request.form)

    try:
        if g.user:
            return redirect( url_for( 'inicio' ) )
        if request.method == 'POST':
            db = get_db()
            error = None
            username = request.form['usuario']
            password = request.form['password']
            passHasheado = generate_password_hash(password)
            print(passHasheado)
            if not username:
                error = 'Debes ingresar el usuario'
                flash( error )
                return render_template( 'login.html' )

            if not password:
                error = 'Contraseña requerida'
                flash( error )
                return render_template( 'login.html' )
    
            user = db.execute(
                'SELECT * FROM usuarios WHERE codigo_usuario = ? AND password = ?', (username, password)
            ).fetchone()
            if user is None:
                user = db.execute(
                    "SELECT * FROM usuarios WHERE codigo_usuario = ?", (username,)
                ).fetchone()
                print(user)
                if user is None:
                    error = 'Usuario no existe'
                else:
                    #Validar contraseña hash            
                    store_password = user[7]    # campo password de la tabla usuarios
                    result = check_password_hash(store_password, password)
                    if result is False:
                        error = 'Contraseña inválida'
                    else:
                        session.clear()
                        session['user_id'] = user[1]    # campo codigo_usuario de la tabla usuarios
                        sesion_iniciada = True
                        usuario = session['user_id']                        
                        return redirect( url_for( 'inicio' ) )
                flash( error )
            else:
                session.clear()
                session['user_id'] = user[1]    # campo codigo_usuario de la tabla usuarios
                if usuario == "SUPERADMIN":
                    return "Pagina de Super Administrador"
                elif usuario == "ADMIN":
                    return render_template("home.html")
                elif usuario == "USER":
                    return redirect( url_for( 'inicio' ) )
            flash( error )
            close_db
        return render_template("login.html", form = login_form)
    except Exception as e:
        print(e)
        return render_template("login.html", form = login_form)


@app.route("/salir", methods=["POST"])
def salir():
    global sesion_iniciada
    sesion_iniciada=False
    return redirect('/')

@app.route("/cancelar", methods=["POST"])
def cancelar():
    global sesion_iniciada
    sesion_iniciada=False
    return redirect('/')


@app.route("/dashboard", methods=["GET", "POST"])
def dashboard():
    # si ya inicio sesion 
    # chequear el perfil
    # segun el perfil mostrar informacion de acuerdo a él.
    return "Dashboard con Informacion del Inventario de Autos segun Perfil" 
    #render_template('index.html')


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
    return render_template('admin.html') 
    # "Administracion de Usuarios"


@app.route('/articulos')
def articulos():
    if g.user:
        sql = "Select * fom productos"
        db = get_db()
        cursor = db.cursor()
        cursor.execute(sql)
        articulos = cursor.fetchall()
        return render_template_string("articulos.html", articulos=articulos)
    else:
        return redirect('login')


@app.route("/productos/<id_productos>", methods=["GET", "POST"])
def productos(id_productos):
    #LogicaAlgoritm Sprint 3
    
    try:
        id_productos= int(id_productos)
    except Exception as e:
        opcion = 0

    if id_productos in Lista_productos:
        return  Lista_productos[id_productos]
    else:
        return  f"Error producto :{id_productos} no existe"


    if id_productos in Lista_productos: 
    # si ya inicio sesion 
    # chequear el perfil
        return  f"Pagina de Gestion de Productos : {id_productos}"
    else:
        return f"Error producto :{id_productos} no existe"
    # si ya inicio sesion 
    # chequear el perfil
    return  "Pagina de Gestion de Productos"
    # Editar / Crear Productos
    # Consulta segun Filtro e Informes
    # render_template('productos.html')


@app.route("/productos/<opcion>", methods=["GET", "POST"])
def gestion_productos(opcion):
    # si ya inicio sesion 
    # chequear el perfil
    opcion = int(opcion)
    if opcion == 1:
        return  "Opcion 1 Editar/Crear Productos"
    else:
        return  "Opcion 2 Consultar Productos"
    # Editar / Crear Productos
    # render_template('gproductos.html')


@app.route("/proveedores/<id_proveedor>", methods=["GET", "POST"]) 
def proveedores(id_proveedor):
    #LogicaAlgoritm Sprint 3
    if id_proveedor in Lista_proveedor: 
    # si ya inicio sesion 
    # chequear el perfil
        return  f"Pagina de Gestion de Proveedores : {id_proveedor}"
    else:
        return f"Error proveedor :{id_proveedor} no existe"
    # Editar / Crear Proveedores
    # render_template('proveedor.html')


@app.route("/proveedor/<opcion>", methods=["GET", "POST"])
def gestion_proveedores(opcion):
    #return  "Opcion 1 Editar/Crear Proveedor"
    # si ya inicio sesion 
    # chequear el perfil

    #LogicaAlgoritm Sprint3
    try:
        opcion= int(opcion)
    except Exception as e:
        opcion = 0

    if opcion in opciones:
        return  opciones[opcion]
    else:
        return  "Opcion Invalida"
    # Editar / Crear Proveedores
    # render_template('gproveedor.html')"""

@app.route("/ayuda", methods=["GET"])
def ayuda():
    # si ya inicio sesion 
    # chequear el perfil
    return  "Manual de Gestión de DAIMLER"
    # Ayuda en General con aceso a Videos.
    # render_template('ayuda.html')


@app.before_request
def load_logged_in_user():
    user_id = session.get( 'user_id' )

    if user_id is None:
        g.user = None
    else:
        g.user = get_db().execute(
            'SELECT * FROM usuarios WHERE codigo_usuario = ?', (user_id,)
        ).fetchone()

@app.route( '/logout' )
def logout():
    session.clear()
    return redirect( url_for( 'inicio' ) )


@app.errorhandler(404)
def page_not_found(error):
    return "Pagina No Encontrada ... ", 404

if __name__ == '__main__':  #Cuando este corriendo de modo principal debe subir el servidor
    app.run() #app.run(debug=True)     #Para que cuando haga un cambio y guarde el servidor se actualiza enseguida