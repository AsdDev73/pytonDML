import pymysql

# Conexión a la base de datos
def conectar():
    return pymysql.connect(
        host='localhost',
        user='root',
        password='Medac123',
        database='acceso_datos_2'
    )

def insertar_registro(tabla):
    conexion = conectar()
    cursor = conexion.cursor()
    try:
        if tabla == '1':
            cursor.execute("INSERT INTO clientes (Nombre, Apellidos, Teléfono, Email, Dirección) VALUES ('Juan D Jose', 'Sanchez', 123456789, 'AJ@example.com', 'Dirección 1')")
        elif tabla == '2':
            cursor.execute("INSERT INTO proveedores (Nombre, Dirección, Teléfono) VALUES ('Nuevo Proveedor', 'Nueva Dirección', 123456789)")
        elif tabla == '3':
            cursor.execute("INSERT INTO almacenes (Espacio, Ubicación) VALUES ('Nuevo Espacio', 'Nueva Ubicación')")
        elif tabla == '4':
            cursor.execute("INSERT INTO gerentes (Nombre, Edad, Teléfono, email) VALUES ('Nuevo Gerente', 50, 123456789, 'gerente@example.com')")
        elif tabla == '5':
            cursor.execute("INSERT INTO empleados (Nombre, Apellido, Puesto, Email, Teléfono, Gerentes_Gerentes_id) VALUES ('Nuevo Empleado', 'Apellido Empleado', 'Puesto Empleado', 'empleado@example.com', 123456789, 1)")
        elif tabla == '6':
            cursor.execute("INSERT INTO categorías (Nombre, Descripción, Productos_Productos_id) VALUES ('Nueva Categoría', 'Descripción Categoría', 1)")
        elif tabla == '7':
            cursor.execute("INSERT INTO productos (Nombre, Precio, Descripción, Proveedores_Proveedores_id, Almacenes_Almacenes_id) VALUES ('Nuevo Producto', 99.99, 'Descripción Producto', 1, 1)")
        conexion.commit()
        print("Registro insertado correctamente.")
    except Exception as e:
        print(f"Error insertando registro en {tabla}: {e}")
        conexion.rollback()
    finally:
        cursor.close()
        conexion.close()

def actualizar_registro(tabla):
    conexion = conectar()
    cursor = conexion.cursor()
    try:
        if tabla == '1':
            cursor.execute("UPDATE clientes SET Email='nuevo_email@example.com' WHERE Nombre='AJ'")
        elif tabla == '2':
            cursor.execute("UPDATE proveedores SET Dirección='Dirección Actualizada' WHERE Nombre='Nuevo Proveedor'")
        elif tabla == '3':
            cursor.execute("UPDATE almacenes SET Ubicación='Ubicación Actualizada' WHERE Espacio='Nuevo Espacio'")
        elif tabla == '4':
            cursor.execute("UPDATE gerentes SET Edad=55 WHERE Nombre='Nuevo Gerente'")
        elif tabla == '5':
            cursor.execute("UPDATE empleados SET Puesto='Puesto Actualizado' WHERE Nombre='Nuevo Empleado'")
        elif tabla == '6':
            cursor.execute("UPDATE categorías SET Descripción='Descripción Actualizada' WHERE Nombre='Nueva Categoría'")
        elif tabla == '7':
            cursor.execute("UPDATE productos SET Precio=88.88 WHERE Nombre='Nuevo Producto'")
        conexion.commit()
        print("Registro actualizado correctamente.")
    except Exception as e:
        print(f"Error actualizando registro en {tabla}: {e}")
        conexion.rollback()
    finally:
        cursor.close()
        conexion.close()

def borrar_registro(tabla):
    conexion = conectar()
    cursor = conexion.cursor()
    try:
        if tabla == '1':
            cursor.execute("DELETE FROM clientes WHERE Nombre='AJ'")
        elif tabla == '2':
            cursor.execute("DELETE FROM proveedores WHERE Nombre='Nuevo Proveedor'")
        elif tabla == '3':
            cursor.execute("DELETE FROM almacenes WHERE Espacio='Nuevo Espacio'")
        elif tabla == '4':
            cursor.execute("DELETE FROM gerentes WHERE Nombre='Nuevo Gerente'")
        elif tabla == '5':
            cursor.execute("DELETE FROM empleados WHERE Nombre='Nuevo Empleado'")
        elif tabla == '6':
            cursor.execute("DELETE FROM categorías WHERE Nombre='Nueva Categoría'")
        elif tabla == '7':
            cursor.execute("DELETE FROM productos WHERE Nombre='Nuevo Producto'")
        conexion.commit()
        print("Registro borrado correctamente.")
    except Exception as e:
        print(f"Error borrando registro en {tabla}: {e}")
        conexion.rollback()
    finally:
        cursor.close()
        conexion.close()

# Consultas
def consulta_like():
    print("Seleccione la tabla en la que desea hacer la consulta LIKE:")
    print("1. Clientes")
    print("2. Proveedores")
    print("3. Almacenes")
    print("4. Productos")
    opcion = input("Seleccione una opción: ")

    conexion = conectar()
    cursor = conexion.cursor()
    try:
        if opcion == '1':
            cursor.execute("""
                SELECT * FROM clientes WHERE Nombre LIKE 'J%'
            """)
        elif opcion == '2':
            cursor.execute("""
                SELECT * FROM proveedores WHERE Nombre LIKE 'P%'
            """)
        elif opcion == '3':
            cursor.execute("""
                SELECT * FROM almacenes WHERE Espacio LIKE 'A%'
            """)
        elif opcion == '4':
            cursor.execute("""
                SELECT * FROM productos WHERE Nombre LIKE 'T%'
            """)
        
        resultados = cursor.fetchall()
        for fila in resultados:
            print(fila)
    except Exception as e:
        print(f"Error ejecutando consulta LIKE en  {e}")
    finally:
        cursor.close()
        conexion.close()
#Metodo select JOIN
def consulta_join():
    print("Seleccione la tabla en la que desea hacer la consulta JOIN:")
    print("1. Productos y Proveedores")
    print("2. Productos y Almacenes") 
    print("3. Empleados y Gerentes") 
    print("4. Pedidos y Clientes")
    opcion = input("Seleccione una opción: ")

    conexion = conectar()
    cursor = conexion.cursor()
    try:
        if opcion == '1':
           cursor.execute("""
            SELECT productos.Nombre, proveedores.Nombre AS Proveedor, productos.Precio
            FROM productos
            JOIN proveedores ON productos.Proveedores_Proveedores_id = proveedores.Proveedores_id
        """)
        elif opcion == '2':
            cursor.execute("""
            SELECT productos.Nombre, almacenes.Espacio AS Almacén, productos.Precio
            FROM productos
            JOIN almacenes ON productos.Almacenes_Almacenes_id = almacenes.Almacenes_id
        """)
        elif opcion == '3':
            cursor.execute("""
            SELECT empleados.Nombre, gerentes.Nombre AS Gerente, empleados.Puesto
            FROM empleados
            JOIN gerentes ON empleados.Gerentes_Gerentes_id = gerentes.Gerentes_id
        """)
        elif opcion == '4':
            cursor.execute("""
            SELECT pedidos.Pedidos_id, clientes.Nombre AS Cliente, pedidos.Estado_pedido
            FROM pedidos
            JOIN clientes ON pedidos.Clientes_Dni = clientes.Dni
        """)

        resultados = cursor.fetchall()
        for fila in resultados:
            print(fila)
    except Exception as e:
        print(f"Error ejecutando consulta group by en  {e}")
    finally:
        cursor.close()
        conexion.close()

#Metodo select group by
def consulta_group_by():

    print("Seleccione la tabla en la que desea hacer la consulta GROUP BY:")
    print("1. Productos")
    print("2. Almacenes")
    print("3. Clientes")
    print("4. Proveedores")
    opcion = input("Seleccione una opción: ")

    conexion = conectar()
    cursor = conexion.cursor()
    try:
        if opcion == '1':
            cursor.execute("""
                SELECT Almacenes_id, COUNT(*)
                FROM productos
                GROUP BY Almacenes_id
            """)
        elif opcion == '2':
            cursor.execute("""
                SELECT Ubicación, COUNT(*)
                FROM almacenes
                GROUP BY Ubicación
            """)
        elif opcion == '3':
            cursor.execute("""
                SELECT Direccion, COUNT(*)
                FROM clientes
                GROUP BY Direccion
            """)
        elif opcion == '4':
            cursor.execute("""
                SELECT Direccion, COUNT(*)
                FROM proveedores
                GROUP BY Direccion
            """)

        resultados = cursor.fetchall()
        for fila in resultados:
            print(fila)
    except Exception as e:
        print(f"Error ejecutando consulta group by en {e}")
    finally:
        cursor.close()
        conexion.close()
# Menú principal
def menu():
    while True:
        print("1. DML con Python")
        print("2. Consultas")
        print("3. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == '1': #submenu DML
            print("1. Insertar registro")
            print("2. Actualizar registro")
            print("3. Borrar registro")
            opcionDML = input("Seleccione una opción: ")

            print("1. Clientes")
            print("2. Proveedores")
            print("3. Almacenes")
            print("4. Gerentes")
            print("5. Empleados")
            print("6. Categorías")
            print("7. Productos")
            tabla = input("Seleccione una tabla: ")

            if tabla:
                if opcionDML == '1':
                    insertar_registro(tabla)
                elif opcionDML == '2':
                    actualizar_registro(tabla)
                elif opcionDML == '3':
                    borrar_registro(tabla)
            else:
                print("Tabla no válida")
        elif opcion == '2':
            print("1. Consulta LIKE")
            print("2. Consulta JOIN")
            print("3. Consulta GROUP BY")
            opcionSelect = input("Seleccione una opción: ")

            if opcionSelect == '1':
                consulta_like()
            elif opcionSelect == '2':
                consulta_join()
            elif opcionSelect == '3':
                consulta_group_by()
        elif opcion == '3':
            print("Saliendo...")
            break
        else:
            print("Opción no válida")

#ejecutar el metodo menu
menu()
