-- Creacion de tablas (DDL)

CREATE TABLE clasificacion_superior (
	codigo varchar(500),
	reino varchar(40),
	filio varchar(40),
	clase varchar(40),
	orden varchar(40),
	familia varchar(40),
	PRIMARY KEY (codigo)
);

CREATE TABLE informacion_taxonomica (
	id_taxonomia varchar(500),
	estado_taxonomico varchar(100),
	observacion_taxonomica varchar(600),
	rango_taxonomico varchar(500),
	codigo_clasificacion varchar(500),
	PRIMARY KEY (id_taxonomia), 
	FOREIGN KEY (codigo_clasificacion) REFERENCES clasificacion_superior (codigo)
);

CREATE TABLE intraespecificidad_epiteto (
	codigo_int integer,
	genero varchar(40),
	epiteto_especifico varchar(40),
	epiteto_intraespecifico varchar(40),
	nombre_vernaculo varchar(500),
	codigo_clasificacion varchar(500),
	PRIMARY KEY (codigo_int),
	FOREIGN KEY (codigo_clasificacion) REFERENCES clasificacion_superior (codigo)
);

CREATE TABLE especies_amenazadas (
	id_nomenclatura varchar(40),
	estado_amenaza varchar(2103),
	intraespecificidad_epiteto integer,
	id_amenaza varchar(500),
	PRIMARY KEY (id_amenaza),
	FOREIGN KEY (intraespecificidad_epiteto) REFERENCES intraespecificidad_epiteto (codigo_int)
);



-- Carga de datos masiva para clasificacion_superior


copy clasificacion_superior from 'C:\Users\Public\Datos\Clasificacion_Supeior.csv' delimiter ',' csv header;


-- Carga de datos masiva para informacion_taxonomica


COPY public.informacion_taxonomica (id_taxonomia, estado_taxonomico, observacion_taxonomica, rango_taxonomico, codigo_clasificacion)
FROM 'C:\Users\Public\Datos\Informacion_Taxonomica1.csv'
DELIMITER ',' CSV HEADER


-- Carga de datos masiva para intraespecificidad_epiteto
	
copy intraespecificidad_epiteto from 'C:\Users\Public\Datos\Intraespecificidad_Epiteto.csv' delimiter ',' csv header;

-- Carga de datos masiva para especies_amenazadas


copy especies_amenazadas from 'C:\Users\Public\Datos\Especies_Amenazadas.csv' delimiter ',' csv header;
