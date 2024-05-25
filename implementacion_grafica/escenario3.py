from dash import Dash, html, dcc
import plotly.express as px
import pandas as pd
import psycopg2

try:
    connection = psycopg2.connect(
        host='localhost',
        user='postgres',
        password='123456789',
        database='pr_final',
        port="5432"
    )
    print("Conexión exitosa")
    cursor = connection.cursor()
    cursor.execute("SELECT reino, filio FROM clasificacion_superior")
    rows = cursor.fetchall()
    
    app = Dash(__name__)
    
    if __name__ == '__main__':
        app.run_server(debug=True)
except Exception as ex:
    print("Error durante la conexión o ejecución:", ex)
finally:
    if cursor:
        cursor.close()
    if connection:
        connection.close()
    print("Conexión finalizada")
