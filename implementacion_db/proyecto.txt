CREATE TABLE clasificacion_superior (
	codigo_tax varchar(20),
	reino varchar(40),
	filio varchar(40),
	clase varchar(40),
	orden varchar(40),
	familia varchar(40),
	idenficacion_tax varchar(60),
	PRIMARY KEY (codigo_tax),
	FOREIGN KEY (identificacion_tax) REFERENCES clasificar
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

CREATE TABLE informacion_taxonomica (
	id_taxonomia varchar(40),
	estado_tax varchar(40),
	observacion_tax varchar(80),
	rango_tax varchar(40),
	PRIMARY KEY (id_taxonomia)
);

CREATE TABLE clasificar (
	identificacion_tax varchar(60),
	id_informacion_tax varchar(40),
	id_taxonomia varchar(40),
	PRIMARY KEY (identificacion_tax),
	FOREIGN KEY (id_taxonomia) REFERENCES informacion_taxonomica
);

CREATE TABLE especies_amenzadas (
	id_nomenclatura varchar(40),
	estado_critico varchar(40),
	codigo_int int,
	PRIMARY KEY (id_nomenclatura),
	FOREIGN KEY (codigo_int) REFERENCES intraespecificidad_epiteto
);