from flask import Flask, render_template
app=Flask(__name__)

opciones=[1,2,3]
usuarios=["SuperAdmin", "Admin", "Usuario"]

@app.route("/", methods=["GET", "POST"])
def inicio():
    # si ya inicio sesion 
    # chequear el perfil
    #
    return render_template('index.html')


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

@app.route("/productos", methods=["GET", "POST"])
def productos():
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


@app.route("/proveedores", methods=["GET", "POST"])
def proveedores():
    # si ya inicio sesion 
    # chequear el perfil
    return  "Pagina de Gestion de Proveedores"
    # Editar / Crear Proveedores
    # render_template('proveedor.html')


@app.route("/proveedores/<opcion>", methods=["GET", "POST"])
def gestion_proveedores(opcion):
    # si ya inicio sesion 
    # chequear el perfil
    opcion = int(opcion)
    if opcion == 1:
        return  "Opcion 1 Editar/Crear Proveedor"
    else:
        return  "Opcion 2 Consultar Proveedores"
    # Editar / Crear Proveedores
    # render_template('gproveedor.html')


@app.route("/ayuda", methods=["GET"])
def ayuda():
    # si ya inicio sesion 
    # chequear el perfil
    return  "Manual de Gestión de DAIMLER"
    # Ayuda en General con aceso a Videos.
    # render_template('ayuda.html')

if __name__ == '__main__':  #Cuando este corriendo de modo principal debe subir el servidor
    app.run(debug=True)     #Para que cuando haga un cambio y guarde el servidor se actualiza enseguida