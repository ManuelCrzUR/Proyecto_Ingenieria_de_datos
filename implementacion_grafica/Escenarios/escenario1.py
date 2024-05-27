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
    cursor.execute("SELECT id_nomenclatura, estado_amenaza, id_amenaza FROM especies_amenazadas")
    rows = cursor.fetchall()
    
    lista_icn = []
    lista_iczn = []
    
    for row in rows:
        if row[0] == 'ICN':
            lista_icn.append(row)
        elif row[0] == 'ICZN':
            lista_iczn.append(row)
        else:
            print("No se puede añadir el dato: ", row)

    # Convertir los resultados a DataFrames de Pandas
    df_icn = pd.DataFrame(lista_icn, columns=['Nomenclatura', 'Estado de Amenaza', 'ID Amenaza'])
    df_iczn = pd.DataFrame(lista_iczn, columns=['Nomenclatura', 'Estado de Amenaza', 'ID Amenaza'])

    # Contar el número de especies en cada estado de amenaza
    df_icn_count = df_icn['Estado de Amenaza'].value_counts().reset_index()
    df_icn_count.columns = ['Estado de Amenaza', 'Número de Especies']

    df_iczn_count = df_iczn['Estado de Amenaza'].value_counts().reset_index()
    df_iczn_count.columns = ['Estado de Amenaza', 'Número de Especies']

    app = Dash(__name__)

    # Definir un diccionario de colores específico para cada estado de amenaza
    color_mapping = {
        'EN': '#FF0000',  # Rojo
        'CR': '#FFA500',  # Naranja
        'VU': '#FFFF00',  # Amarillo
    }

    # Obtener el orden de categorías del primer DataFrame
    category_order = df_icn_count['Estado de Amenaza'].tolist()

    # Crear las gráficas con colores específicos y el mismo orden de categorías
    fig_icn = px.bar(df_icn_count, 
                     x='Estado de Amenaza', 
                     y='Número de Especies', 
                     title='ICN - Número de Especies por Estado de Amenaza',
                     color='Estado de Amenaza',
                     color_discrete_map=color_mapping,
                     category_orders={'Estado de Amenaza': category_order})

    fig_iczn = px.bar(df_iczn_count, 
                      x='Estado de Amenaza', 
                      y='Número de Especies', 
                      title='ICZN - Número de Especies por Estado de Amenaza',
                      color='Estado de Amenaza',
                      color_discrete_map=color_mapping,
                      category_orders={'Estado de Amenaza': category_order})

    # Configurar el fondo transparente para las gráficas
    fig_icn.update_layout({
        'plot_bgcolor': 'rgba(0, 0, 0, 0)',
        'paper_bgcolor': 'rgba(0, 0, 0, 0)',
    })

    fig_iczn.update_layout({
        'plot_bgcolor': 'rgba(0, 0, 0, 0)',
        'paper_bgcolor': 'rgba(0, 0, 0, 0)',
    })

    app.layout = html.Div([
        html.H1("Análisis de Especies Amenazadas"),
        dcc.Graph(figure=fig_icn),
        dcc.Graph(figure=fig_iczn),
        html.P("Con esto concluiríamos el análisis del proyecto esperando que sea de su agrado.")
    ], style={'backgroundColor': '#FFFFFF'})  # Color de fondo de la página

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
