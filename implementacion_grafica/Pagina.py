from dash import Dash, html, dcc
import plotly.express as px
import pandas as pd
import psycopg2

connectio = None
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
    
    app = Dash(__name__)
    
    # Escenario 1
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

    df_icn = pd.DataFrame(lista_icn, columns=['Nomenclatura', 'Estado de Amenaza', 'ID Amenaza'])
    df_iczn = pd.DataFrame(lista_iczn, columns=['Nomenclatura', 'Estado de Amenaza', 'ID Amenaza'])

    df_icn_count = df_icn['Estado de Amenaza'].value_counts().reset_index()
    df_icn_count.columns = ['Estado de Amenaza', 'Número de Especies']

    df_iczn_count = df_iczn['Estado de Amenaza'].value_counts().reset_index()
    df_iczn_count.columns = ['Estado de Amenaza', 'Número de Especies']

    color_mapping = {
        'EN': '#FF0000',  # Rojo
        'CR': '#FFA500',  # Naranja
        'VU': '#FFFF00',  # Amarillo
    }

    category_order = df_icn_count['Estado de Amenaza'].tolist()

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

    fig_icn.update_layout({
        'plot_bgcolor': 'rgba(0, 0, 0, 0)',
        'paper_bgcolor': 'rgba(0, 0, 0, 0)',
    })

    fig_iczn.update_layout({
        'plot_bgcolor': 'rgba(0, 0, 0, 0)',
        'paper_bgcolor': 'rgba(0, 0, 0, 0)',
    })

    # Escenario 2
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
            print("Dato no es posible de añadir")

    df_fungi = pd.DataFrame(lista_f, columns=['Filo'])
    df_plantae = pd.DataFrame(lista_p, columns=['Filo'])
    df_animalia = pd.DataFrame(lista_a, columns=['Filo'])

    fig_fungi = px.pie(df_fungi, names='Filo', title='Fungi - Distribución de Filos', 
                       hover_data={'Filo': True})
    fig_fungi.update_traces(textinfo='label+percent', pull=[0.1, 0.1, 0.1])
    fig_plantae = px.pie(df_plantae, names='Filo', title='Plantae - Distribución de Filos', 
                         hover_data={'Filo': True})
    fig_plantae.update_traces(textinfo='label+percent', pull=[0.1, 0.1, 0.1])
    fig_animalia = px.pie(df_animalia, names='Filo', title='Animalia - Distribución de Filos', 
                          hover_data={'Filo': True})
    fig_animalia.update_traces(textinfo='label+percent', pull=[0.1, 0.1, 0.1])

    # Escenario 3
    cursor.execute("SELECT estado_taxonomico, rango_taxonomico FROM informacion_taxonomica")
    rows = cursor.fetchall()
    
    lista_aceptado = []
    lista_dudoso = []
    lista_sinonimo = []
    lista_valido = []
    
    for row in rows:
        if row[0] == 'Aceptado':
            lista_aceptado.append(row)
        elif row[0] == 'Dudoso':
            lista_dudoso.append(row)
        elif row[0] == 'Sinónimo':
            lista_sinonimo.append(row)
        elif row[0] == 'Válido':
            lista_valido.append(row)
        else:
            print("No se puede añadir el dato: ", row)

    df_aceptado = pd.DataFrame(lista_aceptado, columns=['Estado Taxonómico', 'Rango Taxonómico'])
    df_dudoso = pd.DataFrame(lista_dudoso, columns=['Estado Taxonómico', 'Rango Taxonómico'])
    df_sinonimo = pd.DataFrame(lista_sinonimo, columns=['Estado Taxonómico', 'Rango Taxonómico'])
    df_valido = pd.DataFrame(lista_valido, columns=['Estado Taxonómico', 'Rango Taxonómico'])

    df_aceptado_count = df_aceptado['Rango Taxonómico'].value_counts().reset_index()
    df_aceptado_count.columns = ['Rango Taxonómico', 'Número de Especies']

    df_dudoso_count = df_dudoso['Rango Taxonómico'].value_counts().reset_index()
    df_dudoso_count.columns = ['Rango Taxonómico', 'Número de Especies']

    df_sinonimo_count = df_sinonimo['Rango Taxonómico'].value_counts().reset_index()
    df_sinonimo_count.columns = ['Rango Taxonómico', 'Número de Especies']

    df_valido_count = df_valido['Rango Taxonómico'].value_counts().reset_index()
    df_valido_count.columns = ['Rango Taxonómico', 'Número de Especies']

    fig_aceptado = px.bar(df_aceptado_count, 
                          x='Rango Taxonómico', 
                          y='Número de Especies', 
                          title='Aceptado - Número de Especies por Rango Taxonómico',
                          color='Rango Taxonómico',
                          color_discrete_map=color_mapping,
                          category_orders={'Rango Taxonómico': category_order})

    fig_dudoso = px.bar(df_dudoso_count, 
                        x='Rango Taxonómico', 
                        y='Número de Especies', 
                        title='Dudoso - Número de Especies por Rango Taxonómico',
                        color='Rango Taxonómico',
                        color_discrete_map=color_mapping,
                        category_orders={'Rango Taxonómico': category_order})

    fig_sinonimo = px.bar(df_sinonimo_count, 
                          x='Rango Taxonómico', 
                          y='Número de Especies', 
                          title='Sinónimo - Número de Especies por Rango Taxonómico',
                          color='Rango Taxonómico',
                          color_discrete_map=color_mapping,
                          category_orders={'Rango Taxonómico': category_order})

    fig_valido = px.bar(df_valido_count, 
                        x='Rango Taxonómico', 
                        y='Número de Especies', 
                        title='Válido - Número de Especies por Rango Taxonómico',
                        color='Rango Taxonómico',
                        color_discrete_map=color_mapping,
                        category_orders={'Rango Taxonómico': category_order})

    fig_aceptado.update_layout({
        'plot_bgcolor': 'rgba(0, 0, 0, 0)',
        'paper_bgcolor': 'rgba(0, 0, 0, 0)',
    })

    fig_dudoso.update_layout({
        'plot_bgcolor': 'rgba(0, 0, 0, 0)',
        'paper_bgcolor': 'rgba(0, 0, 0, 0)',
    })

    fig_sinonimo.update_layout({
        'plot_bgcolor': 'rgba(0, 0, 0, 0)',
        'paper_bgcolor': 'rgba(0, 0, 0, 0)',
    })

    fig_valido.update_layout({
        'plot_bgcolor': 'rgba(0, 0, 0, 0)',
        'paper_bgcolor': 'rgba(0, 0, 0, 0)',
    })

    # Escenario 4
    cursor.execute("SELECT genero, nombre_vernaculo FROM intraespecificidad_epiteto")
    rows = cursor.fetchall()
    
    df = pd.DataFrame(rows, columns=['Género', 'Nombre Vernáculo'])

    fig_escenario_4 = px.bar(df, x='Género', y='Nombre Vernáculo', color='Género')

    app.layout = html.Div([
        html.H1("Análisis de Especies Amenazadas"),
        dcc.Graph(figure=fig_icn),
        dcc.Graph(figure=fig_iczn),
        html.P("""
                N:
                    Ventaja: La gráfica nos permite observar cada uno de los estados de amenaza (crítico, vulnerable, en peligro) para las plantas y los animales,
                    y también se observa una mayor cantidad de plantas en estado crítico en comparación a los animales. 
                    Desventaja: Los datos analizados aunque nos muestran la cantidad de especies y su estado de amenaza no nos indica con exactitud cuales
                    son las especies que se encuentran amenazadas solo si son ICN o ICZN.""", style={'padding': '20px', 'font-size' : '27px'}),
        html.P("""
                M:
                    Ventaja: Nos permite visualizar dos gráficos de barra distintos para cada una de las nomenclaturas presentes. 
                    En este caso, es posible representar el comportamiento de cada uno de los estados y la cantidad exacta mediante un hover a cada una de las barras.
                    Desventaja: Personas que no puedan realizar un hover con el mouse, no podrán ver el valor exacto para cada una de las columnas en las gráficas. 
                    Además, es complejo determinar un número total de los datos para cada una de las gráficas. """, style={'padding': '20px', 'font-size' : '27px'}),
        html.P("""
                M:
                    Ventaja: Como se puede ver en la gráfica, las especies mayormente amenazadas son los animales (ICN) que las plantas (ICZN),
                    es decir, su estado de vulnerabilidad es mayor en comparación al de las plantas.
                    Desventaja:  A pesar de que se puede observar un porcentaje aproximado de las especies en cada uno de los estados de amenaza,
                    no se informa la causa de dicha vulnerabilidad tanto en los animales como en las plantas.
            """, style={'padding': '20px', 'font-size' : '27px'}),
        
        html.H1("Distribución de Filos por Reino"),
        html.Div([
            dcc.Graph(figure=fig_fungi),
            dcc.Graph(figure=fig_plantae),
            dcc.Graph(figure=fig_animalia),
        ], style={'color': 'black'}),
        html.P("""
                N:
                    Ventaja: Podemos observar que la gráfica representa la cantidad de filos que se encuentran en cada uno de los reinos, 
                    evidenciando que el reino con la menor cantidad de filos encontrados es el reino fungi, el cual cuenta con un total de 81 especies.
                    Desventaja: La gráfica muestra las especies pero,  no indica específicamente a cuáles de ellas se está haciendo referencia dentro de cada filo, 
                    lo que genera dificultad en determinar sus filos respectivos.""", style={'padding': '20px', 'font-size' : '27px'}),
        html.P("""
                M:
                    Ventajas: Se usa un gráfico apropiado para determinar el total de especies en cada una de las familias presentes en la base de datos, 
                    esto ayuda a las personas consultantes a saber que el gráfico habla de la totalidad de un conjunto de datos determinados. 
                    Es una buena alternativa si se quiere ser más específico en un estudio por familias de las especies en peligro a nivel nacional.
                    Desventajas: En este caso, es muy complicado de determinar e identificar los datos que son pequeños, 
                    dado que por su proporción cuentan con una visibilidad bastante reducida. Es difícil saber la cantidad de datos para cada uno de los filos que se pueden ver en cada una de las gráficas.""", style={'padding': '20px', 'font-size' : '27px'}),
        html.P("""
                M:
                    Ventaja: Similarmente al escenario anterior, se puede determinar de manera precisa el nivel de la afectación en cada reino 
                    (animalia, fungi, plantae) dependiendo de la filo a la que pertenece, en este caso, 
                    se observa que la especie más evidentemente afectada es del reino plantae, por encima del reino animalia y esta a su vez, por encima del reino fungi.
                    Desventaja: No se puede observar claramente los datos pertenecientes a cada reino en el eje x, es decir, que filos pertenecen al reino animalia, cuales al reino fungi y cuales al reino vegetal.
            """, style={'padding': '20px', 'font-size' : '27px'}),
        
        html.H1("Análisis de Rango Taxonómico"),
        dcc.Graph(figure=fig_aceptado),
        dcc.Graph(figure=fig_dudoso),
        dcc.Graph(figure=fig_sinonimo),
        dcc.Graph(figure=fig_valido),
        html.P("""
                N:
                    Ventaja: Según la gráfica, podemos evidenciar que de los rangos taxonómicos (especie, subespecie, variedad)
                    la cifra más elevada en comparación a los demás, es el aceptado, el cual tiene un total de 1283 especies aceptadas según su rango taxonómico  comparación de las subespecies y la variedad.
                    Desventaja: Los datos a analizar no especifican el rango taxonómico al que se hace referencia y a cuál de ellas es su estado taxonómico
                    (aceptado, dudoso, sinónimo, válido), solo lo dice de una forma muy general. """, style={'padding': '20px', 'font-size' : '27px'}),
        html.P("""
                M:
                    Ventajas: La gráfica evidencia que, entre los diferentes rangos taxonómicos (especie, subespecie, variedad), 
                    el estado "aceptado" muestra la cifra más elevada, con un total de 1283 especies según su rango taxonómico. 
                    Esta información permite identificar de manera precisa el rango taxonómico predominante y su aceptación en comparación con subespecies y variedades.
                    Desventajas: La gráfica no especifica de manera clara a qué se refiere cada una de las categorías del estado taxonómico.
                    Esto puede llevar a confusiones al interpretar los datos, ya que no queda explícito qué características o criterios definen cada estado taxonómico en el contexto presentado. """, style={'padding': '20px', 'font-size' : '27px'}),
        html.P("""
                M:
                    Ventaja: Se puede observar que las cifras más altas de la gráfica son las correspondientes al rango de especies,
                    en comparación a los rangos de subespecie y variedad, además de tener en cuenta que dichos datos también son aplicados solamente a los estados aceptado 
                    y válido, ya que en los otros rangos no se tienen especies de esta categoría.
                    Desventaja: No se especifica claramente a que hace referencia cada una de las categorías del estado taxonómico.""", style={'padding': '20px', 'font-size' : '27px'}),
        
        html.H1(children='Gráfico Estado Taxonómico'),
        html.Div(children='''
            Dash: Aplicación para graficar datos
        '''),
        dcc.Graph(id='example-graph', figure=fig_escenario_4),
        html.P("""
                N:
                    Ventaja: Al haber especies sin nombre vernáculo, existe la posibilidad de identificar con mayor facilidad en qué géneros hay especies 
                    que no poseen nombre vernáculo y así enfocarse en ellas de ser necesario.
                    Desventajas: Al tener tantos datos, la gráfica puede desorientar el enfoque que tiene la misma y ser confuso al momento de analizarla. """, style={'padding': '20px', 'font-size' : '27px'}),
        html.P("""
                M:
                    Ventajas: Es fácil de identificar los datos que se encuentran lejos de la media respecto a los máximos, dado que por el hover es fácil reconocer de qué información se trata.
                    Desventajas: Dada la cantidad de datos que se podían encontrar, todos los gráficos cuentan con una dificultad de cómo se ve individualmente y por su proporción,
                    podría ser complicado identificar tantas categorías y barras que se encuentran presente en el gráfico. """, style={'padding': '20px', 'font-size' : '27px'}),
        html.P("""
                M:
                    Ventaja: Permite ver cuántas especies no poseen nombre común, teniendo en cuenta el género al que pertenecen.
                    Desventaja: Es una gran cantidad de datos y es difícil realizar una visualización clara para efectuar un análisis. """, style={'padding': '20px', 'font-size' : '27px'}),

        # Análisis y Conclusiones
        html.Div([
            html.H2("Análisis y Conclusiones"),
            html.H3("CONCLUSIONES"),
            html.P("""
                N:
                    La realización de todo el proyecto se basa en la creación del modelo entidad relación el cual nos permite generalizar la problemática a tratar 
                    y saber cuáles son los temas con mayor relevancia y cómo es que se debe manejar la base de datos a partir de este.
                    La creación de los escenarios permite visualizar el proyecto desde un enfoque diferente ya que permite crear unos casos de estudios donde toca
                    especificar de qué se tratan y a partir de la base de datos que se estudió mirar las relaciones que se pueden realizar entre las tablas.
                    El desarrollo del proyecto fue de manera muy fluida porque entre todos los integrantes del grupo nos entendimos y cuando alguien decía algo se tenía en cuenta y se miraba si era lo mejor.
                    El proyecto sirve mucho porque permite comprender los temas que se analizaron en clase a mayor profundización y así comprenderlo y saber cómo es que se analiza y 
                    se generan las tablas y relaciones a partir de una base de datos.
                    A través de una base de datos se puede analizar muchos temas y se pueden generar diferentes implementaciones según sea la necesidad y lo que se quiere mostrar con la base de datos.
            """, style={'padding': '20px', 'font-size' : '27px'}),
            html.P("""
                M:
                    Se satisface el uso de las herramientas relacionadas con la manipulación de datos, bases de datos, y representación de consultas mediante figuras gráficas.
                    Se encontró una relación con el uso de las herramientas y métodos vistos en clase mediante la posible aplicación en estudios científicos relacionados con biodiversidad 
                    y pérdida de especies en determinado lugar.
                    Se entiende de manera práctica el uso de los datos y ciencia de datos para el entendimiento de cualquier entorno posible siempre que se tengan datos relevantes 
                    sobre los cuales se puedan realizar consultas y análisis estadísticos.
                    Es importante contar con una buena selección de datos, para que la información que se implementa en las bases de datos sea la apropiada y 
                    cuente con relevancia en los estudios en los que se va a aplicar.
            """, style={'padding': '20px', 'font-size' : '27px'}),
            html.P("""
                M:
                    Al finalizar este proyecto, se pudo evidenciar una de las tantas aplicaciones en situaciones de la vida real teniendo en cuenta todo lo visto en clase. 
                    Además se desarrollaron conocimientos más allá del aprendizaje previsto en aula.
                    Por otra parte, se logró sobrepasar con éxito algunos obstáculos que se presentaron a lo largo del desarrollo del trabajo.
                    Desde mi punto de vista, la parte más importante del trabajo fue la selección del tema y la realización de los diagramas entidad relación y modelo relacional.
                    Además, la parte de la creación de las gráficas fue muy dinámica, sin embargo, se tuvo que realizar minuciosamente debido a la cantidad de datos que se tienen en cuenta,
                    especialmente en el último escenario.
                    Finalmente, el trabajo se desarrolló con éxito gracias al buen trabajo en grupo, basándonos en el respeto y teniendo en cuenta las opiniones y sugerencias de cada integrante.
            """, style={'padding': '20px', 'font-size' : '27px'})
        ])
    ], style={'backgroundColor': '#FFFFFF'})

    if __name__ == '__main__':
        app.run_server(debug=False)

except Exception as ex:
    print(ex)
finally:
    connection.close()
    print("Conexión finalizada")