from flask import Flask, render_template
from flask import redirect, request

app=Flask(__name__)

opciones={
    1: "Editar/Crear proveedores",
    2: "Consultar Proveedores",
    3: "Eliminar Proveedores"}

usuarios=["SUPERAD", "ADMIN", "USER"]

Lista_productos={
    1001: "BMWi3",
    2001: "KIA NEW SPORTAGE 2.0",
    3001: "FORD EXPLORER LIMITED 3.5",
    4001: "Audi A5 Sportbag",
    5001: "Mercedes Benz E200"}

Lista_proveedor=["BMW", "Audi", "Subaru", "Kia", "FORD", "Mercedes Benz"] 

sesion_iniciada=False

@app.route("/", methods=["GET"])
def inicio():
    # si ya inicio sesion 
    # chequear el perfil
    # segun el perfil lo envia a la pagina segun Mapa de Navegabilidad

    return render_template('index.html', sesion_iniciada=sesion_iniciada)


@app.route("/login", methods=["GET", "POST"])
def login():
    global sesion_iniciada
    if request.method=="GET":
        return render_template("login.html")
    else:
        sesion_iniciada=True
        return redirect('/')


@app.route("/salir", methods=["POST"])
def salir():
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

if __name__ == '__main__':  #Cuando este corriendo de modo principal debe subir el servidor
    app.run(debug=True)     #Para que cuando haga un cambio y guarde el servidor se actualiza enseguida