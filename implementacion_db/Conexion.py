import psycopg2
import pandas as pd

connection = None  # Inicializa la variable connection fuera del bloque try

try:
    connection = psycopg2.connect(
       host="localhost",
       database="repaso", #el nombre que se le haya puesto al DB al crearlo en sql
       user="postgres",
       password="123456789" #poner contraseña propia
   )
    print('Conexión exitosa')
    
    cursor = connection.cursor()
    
#Tabla1 CLASIFICACIÓN SUPERIOR
    query_tabla1 = "Select * From clasificacion_superior;"
    cursor.execute(query_tabla1)
    tipo_clasificacion = cursor.fetchall() #Lista de tuplas con la info de la tabla. No están los nombres de las colunas de la tabla tipo_empleo
   
    columnas = [desc[0] for desc in cursor.description]
    #El atributo .description da una lista de tuplas con informacion de la conexión. En las primeras poscición con indice 0 aparecen los nombres de las columnas
    
    tipo_clasificacionDF = pd.DataFrame(tipo_clasificacion, columns=columnas) #df de la primera tabla
   
    for clasificacion in tipo_clasificacion:
        print(clasificacion) #Imprime cada tupla de la tabla tipo de empleo
        

#Tabla2 INFORMACIÓN TAXONOMICA
    query_tabla2 = "Select * From informacion_taxonomica;"
    cursor.execute(query_tabla2)
    tipo_info = cursor.fetchall() #Lista de tuplas con la info de la tabla. No están los nombres de las colunas de la tabla tipo_empleo
   
    columnas = [desc[0] for desc in cursor.description]
    #El atributo .description da una lista de tuplas con informacion de la conexión. En las primeras poscición con indice 0 aparecen los nombres de las columnas
    
    tipo_infoDF = pd.DataFrame(tipo_info, columns=columnas) #df de la primera tabla
   
    for taxonomia in tipo_info:
        print(taxonomia) #Imprime cada tupla de la tabla tipo de empleo
        
#Tabla3 INTRAESPECIFICIDAD EPITETO
    query_tabla3 = "Select * From intraespecificidad_epiteto;"
    cursor.execute(query_tabla3)
    tipo_intra = cursor.fetchall() #Lista de tuplas con la info de la tabla. No están los nombres de las colunas de la tabla tipo_empleo
   
    columnas = [desc[0] for desc in cursor.description]
    #El atributo .description da una lista de tuplas con informacion de la conexión. En las primeras poscición con indice 0 aparecen los nombres de las columnas
    
    tipo_intraDF = pd.DataFrame(tipo_intra, columns=columnas) #df de la primera tabla
   
    for epi in tipo_clasificacion:
        print(epi) #Imprime cada tupla de la tabla tipo de empleo
        
#Tabla4 ESPECIES AMENAZADAS
    query_tabla4 = "Select * From especies_amenazadas;"
    cursor.execute(query_tabla3)
    tipo_esp = cursor.fetchall() #Lista de tuplas con la info de la tabla. No están los nombres de las colunas de la tabla tipo_empleo
   
    columnas = [desc[0] for desc in cursor.description]
    #El atributo .description da una lista de tuplas con informacion de la conexión. En las primeras poscición con indice 0 aparecen los nombres de las columnas
    
    tipo_espDF = pd.DataFrame(tipo_esp, columns=columnas) #df de la primera tabla
   
    for especies in tipo_esp:
        print(especies) #Imprime cada tupla de la tabla tipo de empleo

except Exception as ex:
    print(ex)

finally:
    if connection is not None:  # Verifica si la conexión se estableció correctamente
        connection.close()  # Cierra la conexión solo si se estableció correctamente
        print("Conexión cerrada")  # Mensaje de confirmación de cierre de conexión
