import sqlite3

#Conexión a la Base de Datos
con = sqlite3.connect('db/daimler.db')

#Creando cursor
pibote = con.cursor()

#Creando la tabla
try:
    pibote.execute ("""
CREATE TABLE usuarios (
  id_usuario INTEGER PRIMARY KEY AutoIncrement,
  codigo_usuario varchar(15) NOT NULL UNIQUE,
  nombre_usuario varchar(255) NOT NULL,
  email_usuario varchar(255) NOT NULL,
  cargo varchar(15) DEFAULT NULL,
  foto varchar(100) DEFAULT NULL,
  codigo_rol varchar(15) NOT NULL,
  password varchar(50) NOT NULL,
  codigo_pais varchar(15) DEFAULT NULL,
  direccion varchar(255) DEFAULT NULL,
  telefono varchar(50) NOT NULL,
  celular varchar(50) NOT NULL,
  ciudad varchar(50) DEFAULT NULL,
  fecha_ult_con datetime DEFAULT NULL,
  intentos decimal(15,0) DEFAULT NULL,
  bloqueo decimal(15,0) DEFAULT NULL,
  fecha_usuario datetime DEFAULT NULL,
  fecha_password datetime DEFAULT NULL,
  estado char(1) NOT NULL DEFAULT 1
  );
    """)
except Exception as e:
    print(e)

try:
    pibote.execute ("""
CREATE TABLE fabricante (
  id_fabricante INTEGER PRIMARY KEY AutoIncrement,
  cod_fabricante varchar(15) NOT NULL UNIQUE,
  tipoid_fabricante varchar(5) NOT NULL,
  nroid_fabricante varchar(15) NOT NULL,
  dv_nroid char(1) NOT NULL,
  razon_social_fabricante varchar(255) NOT NULL,
  nombre_representante varchar(255) NOT NULL,
  nombre_contacto varchar(255) NOT NULL,
  email_fabricante varchar(255) NOT NULL,
  codigo_pais varchar(15) DEFAULT NULL,
  ciudad varchar(50) DEFAULT NULL,
  direccion varchar(255) DEFAULT NULL,
  telefono varchar(50) NOT NULL,
  celular varchar(50) NOT NULL,
  estado char(1) NOT NULL DEFAULT 1,
  fecha_sistema datetime DEFAULT NULL,
  codigo_usuario varchar(15) NOT NULL
  );
    """)
except Exception as e:
    print(e)


try:
    pibote.execute ("""
CREATE TABLE productos (
  id_producto INTEGER PRIMARY KEY AutoIncrement,
  codigo_producto varchar(15) NOT NULL UNIQUE,
  nombre_producto varchar(255) NOT NULL,
  descripcion text,
  cminima_rq_bodega decimal(15,0) DEFAULT NULL,
  cdisponible_bodega decimal(15,0) DEFAULT NULL,
  estado char(1) NOT NULL DEFAULT 1,
  fecha_sistema datetime DEFAULT NULL,
  codigo_usuario varchar(15) NOT NULL
  );
    """)
except Exception as e:
    print(e)

try:
    pibote.execute ("""
CREATE TABLE autos (
  id_auto INTEGER PRIMARY KEY AutoIncrement,
  codigo_auto varchar(15) NOT NULL UNIQUE,
  nombre_auto varchar(255) NOT NULL,
  descripcion text,
  modelo int(11) NOT NULL DEFAULT 2000, 
  id_fabricante int(11) DEFAULT NULL REFERENCES fabricante(id_fabricante) ON DELETE NO ACTION ON UPDATE CASCADE,
  linea varchar(15) DEFAULT NULL,
  estado char(1) NOT NULL DEFAULT 1,
  fecha_sistema datetime DEFAULT NULL,
  codigo_usuario varchar(15) NOT NULL
  );
    """)
except Exception as e:
    print(e)

try:
    pibote.execute ("""
CREATE TABLE proveedor (
  id_proveedor INTEGER PRIMARY KEY AutoIncrement,
  codigo_proveedor varchar(15) NOT NULL UNIQUE,
  tipoid_proveedor varchar(5) NOT NULL,
  nroid_proveedor varchar(15) NOT NULL,
  dv_nroid char(1) NOT NULL,
  razon_social_proveedor varchar(255) NOT NULL,
  nombre_representante varchar(255) NOT NULL,
  nombre_contacto varchar(255) NOT NULL,
  email_proveedor varchar(255) NOT NULL,
  codigo_pais varchar(15) DEFAULT NULL,
  ciudad varchar(50) DEFAULT NULL,
  direccion varchar(255) DEFAULT NULL,
  telefono varchar(50) NOT NULL,
  celular varchar(50) NOT NULL,
  estado char(1) NOT NULL DEFAULT 1,
  fecha_sistema datetime DEFAULT NULL,
  codigo_usuario varchar(15) NOT NULL
  );
    """)
except Exception as e:
    print(e)


try:
    pibote.execute ("""
CREATE TABLE menu (
  idmenu varchar(10) NOT NULL UNIQUE,
  desc_menu varchar(100) DEFAULT NULL,
  ayuda text,
  metodo varchar(100) DEFAULT NULL,
  nivel_1 decimal(10,0) DEFAULT NULL,
  nivel_2 decimal(10,0) DEFAULT NULL,
  nivel_3 decimal(10,0) DEFAULT NULL,
  activo char(1) NOT NULL DEFAULT 0,
  PRIMARY KEY (idmenu)
);
    """)
except Exception as e:
    print(e)

try:
    pibote.execute ("""
CREATE TABLE menu_rol (
  idmenu varchar(10) NOT NULL,
  codigo_rol varchar(15) NOT NULL,
  desc_menu varchar(100) DEFAULT NULL,
  nivel_1 decimal(10,0) DEFAULT NULL,
  nivel_2 decimal(10,0) DEFAULT NULL,
  nivel_3 decimal(10,0) DEFAULT NULL,
  activo char(1) NOT NULL DEFAULT 0,
  PRIMARY KEY (idmenu,codigo_rol)
); 
    """)
except Exception as e:
    print(e)

try:
    pibote.execute ("""
CREATE TABLE roles (
  codigo_rol varchar(15) NOT NULL,
  nombre_rol varchar(255) NOT NULL,
  prioridad decimal(10,0) NOT NULL DEFAULT 1,
  PRIMARY KEY (codigo_rol)
);
    """)
except Exception as e:
    print(e)

try:
    pibote.execute ("""
CREATE TABLE produ_auto (
  id_producto int NOT NULL,
  id_auto int NOT NULL,
  fecha_sistema datetime DEFAULT NULL REFERENCES productos(id_producto) ON DELETE RESTRICT ON UPDATE CASCADE,
  codigo_usuario varchar(15) NOT NULL REFERENCES autos(id_auto) ON DELETE RESTRICT ON UPDATE CASCADE,
  PRIMARY KEY (id_producto, id_auto)
);
    """)
except Exception as e:
    print(e)

try:
    pibote.execute ("""
CREATE TABLE produ_prov (
  id_producto int NOT NULL REFERENCES productos(id_producto) ON DELETE RESTRICT ON UPDATE CASCADE,
  id_proveedor int NOT NULL REFERENCES proveedor(id_proveedor) ON DELETE RESTRICT ON UPDATE CASCADE,
  fecha_sistema datetime DEFAULT NULL,
  codigo_usuario varchar(15) NOT NULL,
  PRIMARY KEY (id_producto, id_proveedor)
);
    """)
except Exception as e:
    print(e)

try:
    pibote.execute ("""
create UNIQUE INDEX codfab_UNIQUE on fabricante(cod_fabricante);
    """)
except Exception as e:
    print(e)


try:
    pibote.execute ("""
create UNIQUE INDEX codprov_UNIQUE on proveedor(codigo_proveedor);
    """)
except Exception as e:
    print(e)

try:
    pibote.execute ("""
create UNIQUE INDEX cod_auto_UNIQUE on autos(codigo_auto);
    """)
except Exception as e:
    print(e)

try:
    pibote.execute ("""
create UNIQUE INDEX cod_producto_UNIQUE on productos(codigo_producto);
    """)
except Exception as e:
    print(e)

try:
    pibote.execute ("""
create UNIQUE INDEX codigo_usuario_UNIQUE on usuarios(codigo_usuario);
    """)
except Exception as e:
    print(e)


try: 
    pibote.execute("""
    INSERT INTO autos (id_fabricante, codigo_auto, nombre_auto, descripcion, modelo, linea, estado, codigo_usuario) 
    VALUES (5, '112345789', 'TOYOTA LAND CRUISER LC300', 'La versión más lujosa del todoterreno japonés', 2021, 'Todoterreno', 1, 'Administrador'),
           (3, '113335889', 'ALFA ROMEO STELVIO GT JUNIOR', 'El moderno SUV se viste de edición especial y acabados del nivel Veloce', 2021, 'Coupé', 1, 'Administrador'),
           (4, '111355689', 'Toyota Corolla Cross', 'Un SUV compacto que vendrá a reforzar aún más la oferta de híbridos en el país', 2021, 'SUV', 1, 'Administrador'),
           (2, '114325989', 'Chevrolet Spark 2019', 'Mayor calidad, más potencia y mejor equipamiento', 2019, 'Urbano', 1, 'SuperAdministrador'),
           (1, '110365589', 'HYUNDAI ACCENT 2020', 'Sus cambios más importantes buscan mejorar el ahorro de combustible', 2020, 'Sedan', 1, 'Administrador'); 
    """)
except Exception as e:
    print(e)

try: 
    pibote.execute("""
    INSERT INTO usuarios (codigo_usuario, nombre_usuario, email_usuario, cargo, foto, codigo_rol,
                password, codigo_pais, direccion, telefono, celular, ciudad, fecha_ult_con, intentos, bloqueo,
                fecha_usuario, fecha_password, estado ) 
    VALUES ('Administrador', 'ADMIN', 'admin@daimler.com.co', 'Administrador', '', 'ADMIN', '1357924680', 'CO', 'CALLE con CRA', '3012011234', '3012011234', 'BAQ', datetime('now'),1,0,datetime('now'), datetime('now'), '1' ),
           ('SuperAdministrador', 'SUPERADMIN', 'superadmin@daimler.com.co', 'Super Administrador', '', 'SADMIN', '1357924680', 'CO', 'CALLE con CRA', '3012011234', '3012011234', 'BAQ', datetime('now'),1,0,datetime('now'), datetime('now'), '1' ),
           ('Usuario', 'USUARIO', 'user@daimler.com.co', 'Usuario Final', '', 'USER', '1357924680', 'CO', 'CALLE con CRA', '3012011234', '3012011234', 'BAQ', datetime('now'),1,0,datetime('now'), datetime('now'), '1' )
    """)
except Exception as e:
    print(e)


try: 
    pibote.execute("""
    INSERT INTO roles (codigo_rol, nombre_rol, prioridad) 
    VALUES ('ADMIN', 'Administrador', 100),
           ('SADMIN', 'Super Administrador', 200),
           ('USER', 'Usuario Final', 10)
    """)
except Exception as e:
    print(e)

con.commit()

con.close()