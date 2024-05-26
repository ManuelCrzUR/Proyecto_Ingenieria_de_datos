from dash import Dash, html, dcc
import plotly.express as px
import pandas as pd
import psycopg2

try:
    connection = psycopg2.connect(
        host='localhost',
        user='postgres',
        password='123456789',
        database='Proyecto2',
        port="5432"
    )
    print("Conexión exitosa")
    cursor = connection.cursor()
    cursor.execute("select estado_taxonomico, rango_taxonomico from informacion_taxonomica")
    rows = cursor.fetchall()
    
    lista_Aceptado = []
    lista_Dudoso = []
    lista_Sinonimo = []
    lista_Valido = []
    
    for row in rows:
        if row[0] == 'Acepado':
            lista_Aceptado.append(row)
        elif row[0] == 'Dudoso':
            lista_Dudoso.append(row)
        elif row[0] == 'Sinonimo':
            lista_Sinonimo.append(row)
        elif row[0] == 'Valido':
            lista_Valido.append(row)
        else:
            print("No se puede añadir el dato: ", row)

    # Convertir los resultados a DataFrames de Pandas
    df_Aceptado = pd.DataFrame(lista_Aceptado, columns=[ 'id_taxonomia','estado_taxonomico','observacion_taxonomica',' rango_taxonomico','codigo_clasificacion'])
    df_Dudoso = pd.DataFrame(lista_Dudoso, columns=[ 'id_taxonomia','estado_taxonomico','observacion_taxonomica',' rango_taxonomico','codigo_clasificacion'])
    df_Sinonimo = pd.DataFrame(lista_Sinonimo, columns=[ 'id_taxonomia','estado_taxonomico','observacion_taxonomica',' rango_taxonomico','codigo_clasificacion'])
    df_Valido = pd.DataFrame(lista_Valido, columns=[ 'id_taxonomia','estado_taxonomico','observacion_taxonomica',' rango_taxonomico','codigo_clasificacion'])
            
    
    # Contar el número de especies en cada estado de amenaza
    df_Aceptado_count = df_Aceptado['rango_taxonomico'].value_counts().reset_index()
    df_Aceptado_count.columns = ['rango_taxonomico', 'Número de Especies']

    df_Dudoso_count = df_Dudoso['rango_taxonomico'].value_counts().reset_index()
    df_Dudoso_count.columns = ['rango_taxonomico', 'Número de Especies']

    df_Sinonimo_count = df_Sinonimo['rango_taxonomico'].value_counts().reset_index()
    df_Sinonimo_count.columns = ['rango_taxonomico', 'Número de Especies']
     
    df_Valido_count = df_Valido['rango_taxonomico'].value_counts().reset_index()
    df_Valido_count.columns = ['rango_taxonomico', 'Número de Especies']
    app = Dash(_name_)

    # Definir un diccionario de colores específico para cada estado de amenaza
    color_mapping = {
        'EN': '#FF0000',  # Rojo
        'CR': '#FFA500',  # Naranja
        'VU': '#FFFF00',  # Amarillo
    }

    # Obtener el orden de categorías del primer DataFrame
    category_order = df_Aceptado_count['rango_taxonomico'].tolist()

    # Crear las gráficas con colores específicos y el mismo orden de categorías
    fig_Aceptado = px.bar(df_Aceptado_count, 
                     x='rango_taxonomico', 
                     y='Número de Especies', 
                     title='rango_taxonomico - Número de Especies por Estado de Amenaza',
                     color='Estado de Amenaza',
                     color_discrete_map=color_mapping,
                     category_orders={'Estado de Amenaza': category_order})

    fig_Dudoso = px.bar(df_Dudoso_count, 
                      x='rango_taxonomico', 
                      y='Número de Especies', 
                      title='ICZN - Número de Especies por Estado de Amenaza',
                      color='Estado de Amenaza',
                      color_discrete_map=color_mapping,
                      category_orders={'Estado de Amenaza': category_order})

    fig_Sinonimo = px.bar(df_Sinonimo_count, 
                      x='rango_taxonomico', 
                      y='Número de Especies', 
                      title='ICZN - Número de Especies por Estado de Amenaza',
                      color='Estado de Amenaza',
                      color_discrete_map=color_mapping,
                      category_orders={'Estado de Amenaza': category_order})
   
    fig_Valido = px.bar(df_Valido_count, 
                      x='rango_taxonomico', 
                      y='Número de Especies', 
                      title='ICZN - Número de Especies por Estado de Amenaza',
                      color='Estado de Amenaza',
                      color_discrete_map=color_mapping,
                      category_orders={'Estado de Amenaza': category_order})


    # Configurar el fondo transparente para las gráficas
    fig_Aceptado.update_layout({
        'plot_bgcolor': 'rgba(0, 0, 0, 0)',
        'paper_bgcolor': 'rgba(0, 0, 0, 0)',
    })

    fig_Dudoso.update_layout({
        'plot_bgcolor': 'rgba(0, 0, 0, 0)',
        'paper_bgcolor': 'rgba(0, 0, 0, 0)',
    })
    
    fig_Sinonimo.update_layout({
        'plot_bgcolor': 'rgba(0, 0, 0, 0)',
        'paper_bgcolor': 'rgba(0, 0, 0, 0)',
    })
    
    fig_Valido.update_layout({
        'plot_bgcolor': 'rgba(0, 0, 0, 0)',
        'paper_bgcolor': 'rgba(0, 0, 0, 0)',
    })

    app.layout = html.Div([
        html.H1("Análisis de Rango Taxonomico"),
        dcc.Graph(figure=fig_Aceptado),
        dcc.Graph(figure=fig_Dudoso),
        dcc.Graph(figure=fig_Sinonimo),
        dcc.Graph(figure=fig_Valido),
        html.P("Con esto concluiríamos el análisis del proyecto esperando que sea de su agrado.")
    ], style={'backgroundColor': '#FFFFFF'})  # Color de fondo de la página

    if _name_ == '_main_':
        app.run_server(debug=True)
        
        
except Exception as ex:
    print("Error durante la conexión o ejecución:", ex)
finally:
    if cursor:
        cursor.close()
    if connection:
        connection.close()
        

    print("Conexión finalizada")
