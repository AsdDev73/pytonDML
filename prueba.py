#1. Importar la librería
import pymysql

#2. Conexión a base de datos
#Crear previamente la base de datos basedatos en MYSQLWORKBENCH
#connect(host,user,password,basededatos)
connection = pymysql.connect(host="localhost",user="root",passwd="Medac123",database="acceso")

#3. Escribimos la consulta en una variable
#consulta DML (select,insert,update,delete)
sql_query = "SELECT VERSION()"

#4. Dentro try..except. Creamos cursor y ejecutamos consulta DML
try:
    #Obtenemos el objeto cursor. Un cursor guarda el resultado de una consulta
    cursor = connection.cursor()
    
    #5. Ejecutamos la consulta
    cursor.execute(sql_query)
    #fetchone(). Obtenemos una fila. 
    #fetchall(). Obtenemos todas las filas
    #rowcount(). Devuelve el  número de filas
    datos = cursor.fetchone()
    print("Versión Base Datos MySQL: ",datos)
    #6. En caso de insert,update,delete hacemos commit: connection.commit() 
except Exception as e:
    print("Exception: ",e)
    #6. En caso de insert,update,delete hacemos commit: connection.commit() 

#7. Cerramos conexión
connection.close()
