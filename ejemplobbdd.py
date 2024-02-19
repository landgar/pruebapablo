import sqlite3

# Conexión
nombrebbdd="bd1.db"
conexion=sqlite3.connect(nombrebbdd)

# Creación de tabla
try:
    conexion.execute("""create table articulos (
                              codigo integer primary key autoincrement,
                              descripcion text,
                              precio real
                        )""")
    print("se creo la tabla articulos")
except sqlite3.OperationalError:
    print("La tabla articulos ya existe")
conexion.close()

# Inserción de datos a la tabla
conexion=sqlite3.connect(nombrebbdd)
conexion.execute("insert into articulos(descripcion,precio) values (?,?)", ("naranjas", 23.50))
conexion.execute("insert into articulos(descripcion,precio) values (?,?)", ("peras", 34))
conexion.execute("insert into articulos(descripcion,precio) values (?,?)", ("bananas", 25))
conexion.commit()
conexion.close()

# Lectura de datos de la tabla: todas las filas
conexion=sqlite3.connect(nombrebbdd)
cursor=conexion.execute("select codigo,descripcion,precio from articulos")
for fila in cursor:
    print(fila)
conexion.close()

# Lectura de datos de la tabla: filtro de datos: una fila
conexion=sqlite3.connect(nombrebbdd)
codigo=int(input("Ingrese el código de un artículo:"))
cursor=conexion.execute("select descripcion,precio from articulos where codigo=?", (codigo, ))
fila=cursor.fetchone()
if fila!=None:
    print(fila)
else:
    print("No existe un artículo con dicho código.")
conexion.close()


# Lectura de datos de la tabla: filtro de datos: varias filas
conexion=sqlite3.connect(nombrebbdd)
precio=float(input("Ingrese un precio (se obtendrán los artículos con precio mejor que el indicado):"))
cursor=conexion.execute("select descripcion from articulos where precio<?", (precio, ))
filas=cursor.fetchall()
if len(filas)>0:
    for fila in filas:
        print(fila)
else:
    print("No existen artículos con un precio menor al ingresado.")
conexion.close()
