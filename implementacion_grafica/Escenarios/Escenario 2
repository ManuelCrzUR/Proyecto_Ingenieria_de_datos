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
    
    lista_a = []
    lista_p = []
    lista_f = []
    
    for row in rows:
        if row[0] == 'Fungi':
            lista_f.append(row[1])
        elif row[0] == 'Plantae':
            lista_p.append(row[1])
        elif row[0] == 'Animalia':
            lista_a.append(row[1])
        else:
            print("dato no es posible de añadir")

    # Contar la frecuencia de cada filo en cada reino
    df_fungi = pd.DataFrame(lista_f, columns=['Filo'])
    df_plantae = pd.DataFrame(lista_p, columns=['Filo'])
    df_animalia = pd.DataFrame(lista_a, columns=['Filo'])

    fig_fungi = px.pie(df_fungi, names='Filo', title='Fungi - Distribución de Filos', 
                       hover_data={'Filo': True})
    fig_fungi.update_traces(textinfo='label+percent', pull=[0.1, 0.1, 0.1])  # Agregar etiquetas de datos
    fig_plantae = px.pie(df_plantae, names='Filo', title='Plantae - Distribución de Filos', 
                        hover_data={'Filo': True})
    fig_plantae.update_traces(textinfo='label+percent', pull=[0.1, 0.1, 0.1])  # Agregar etiquetas de datos
    fig_animalia = px.pie(df_animalia, names='Filo', title='Animalia - Distribución de Filos', 
                         hover_data={'Filo': True})
    fig_animalia.update_traces(textinfo='label+percent', pull=[0.1, 0.1, 0.1])  # Agregar etiquetas de datos

    app = Dash(__name__)

    app.layout = html.Div([
        html.H1("Distribución de Filos por Reino"),
        html.Div([
            dcc.Graph(figure=fig_fungi),
            dcc.Graph(figure=fig_plantae),
            dcc.Graph(figure=fig_animalia)
        ])
    ])

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
