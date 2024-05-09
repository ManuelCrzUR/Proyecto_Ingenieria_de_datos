CREATE TABLE clasificacion_superior (
	codigo integer,
	reino varchar(40),
	filio varchar(40),
	clase varchar(40),
	orden varchar(40),
	familia varchar(40),
	PRIMARY KEY (codigo)
);

CREATE TABLE informacion_taxonomica (
	id_taxonomia varchar(40),
	estado_taxonomico varchar(40),
	observacion_taxonomica varchar(80),
	rango_taxonomico varchar(40),
	codigo_clasificacion integer,
	PRIMARY KEY (id_taxonomia), 
	FOREIGN KEY (codigo_clasificacion) REFERENCES clasificacion_superior
);

CREATE TABLE intraespecificidad_epiteto (
	codigo_int int,
	genero varchar(40),
	epiteto_especifico varchar(40),
	epiteto_intraespecifico varchar(40),
	nombre_vernaculo varchar(60),
	PRIMARY KEY (codigo_int),
	FOREIGN KEY (codigo_tax) REFERENCES clasificacion_superior
);