


CREATE SCHEMA roomy;

/*1*/
CREATE TABLE roomy.roles (
  id_rol         SERIAL PRIMARY KEY,
  codigo         TEXT NOT NULL UNIQUE,
  descripcion    TEXT NOT NULL
);

CREATE TABLE roomy.usuarios (

id                        SERIAL PRIMARY KEY,
rol                       INTEGER REFERENCES roomy.roles(id_rol) NOT NULL,
nombre                    TEXT NOT NULL,
correo                    TEXT NOT NULL,
telefono                  INTEGER NOT NULL,
alias                     TEXT NOT NULL,
foto                      TEXT NOT NULL,
en_casa                   BOOLEAN NOT NULL,
merito                    INTEGER NOT NULL,
demerito                  INTEGER NOT NULL ,
puntaje                   INTEGER NOT NULL,
fecha_creacion            TIMESTAMP NOT NULL,
fecha_actualizacion       TIMESTAMP NOT NULL
);


CREATE TABLE roomy.status (
  
 id_status      SERIAL PRIMARY KEY,
 codigo         TEXT NOT NULL UNIQUE,
 descripcion    TEXT NOT NULL

);
/*pendiente termindao due, perdido, apartado, encontrado,proximo, en curso, terminada*/

CREATE TABLE roomy.tipo (
  
 id_tipo        SERIAL PRIMARY KEY,
 codigo         TEXT NOT NULL UNIQUE,
 descripcion    TEXT NOT NULL

);
/* queja,  sugerencia, general, repuesta, urgencia*/

/*2*/
CREATE TABLE roomy.pagos (
  
id                  SERIAL PRIMARY KEY,
status              INTEGER REFERENCES roomy.status(id_status) NOT NULL,
nombre              TEXT NOT NULL,
descripcion         TEXT NOT NULL,
foto                TEXT NOT NULL,
creado_por          INTEGER REFERENCES roomy.usuarios(id) NOT NULL,
responsables        TEXT [],
valor               INTEGER,
realizadopor        TEXT [],
pendientepara       TEXT [],
fecha_comienzo      DATE NOT NULL,
fecha_fin           DATE NOT NULL,
fecha_creacion      TIMESTAMP NOT NULL,
fecha_actualizacion TIMESTAMP NOT NULL

);

/*3*/

CREATE TABLE roomy.queHaceres (
id                  SERIAL PRIMARY KEY,
status              INTEGER REFERENCES roomy.status(id_status) NOT NULL,
nombre             TEXT NOT NULL,
descripcion         TEXT NOT NULL,
foto                TEXT NOT NULL,
creado_por          INTEGER REFERENCES roomy.usuarios(id) NOT NULL,
responsables        TEXT [],
fecha_comienzo      DATE NOT NULL,
fecha_fin           DATE NOT NULL,
fecha_creacion      TIMESTAMP NOT NULL,
fecha_actualizacion TIMESTAMP NOT NULL,
valor               INTEGER  
);


/*4*/
CREATE TABLE roomy.pertenencia (
 
id           SERIAL PRIMARY KEY,
creado_por   INTEGER REFERENCES roomy.usuarios(id) NOT NULL,
status       INTEGER REFERENCES roomy.status(id_status) NOT NULL,
nombre       TEXT NOT NULL,
descripcion  TEXT NOT NULL,
tipo         TEXT NOT NULL,
foto         TEXT NOT NULL

);



/*5*/
CREATE TABLE roomy.eventos (
  
id            SERIAL PRIMARY KEY,
status        INTEGER REFERENCES roomy.status(id_status) NOT NULL, 
nombre        TEXT NOT NULL,
creado_por    INTEGER REFERENCES roomy.usuarios(id) NOT NULL,
descripcion   TEXT NOT NULL,
tipo          TEXT NOT NULL,
foto          TEXT NOT NULL

);


/*6*/

CREATE TABLE roomy.compartibles (
  
id                 SERIAL PRIMARY KEY,
status             INTEGER REFERENCES roomy.status(id_status) NOT NULL,
nombre             TEXT NOT NULL,
descripcion        TEXT NOT NULL,
foto               TEXT NOT NULL,
creado_por         INTEGER REFERENCES roomy.usuarios(id) NOT NULL,
involucrados       DATE NOT NULL,
fecha_fin          DATE NOT NULL,
fecha_creacion     TIMESTAMP NOT NULL,
fecha_actualizacion TIMESTAMP NOT NULL,
valor              INTEGER  

);


/*7*/
CREATE TABLE roomy.comentarios (
  
id                  SERIAL PRIMARY KEY,
tipo                INTEGER REFERENCES roomy.tipo(id_tipo) NOT NULL,
Idparent            INTEGER REFERENCES roomy.comentarios(id),
Foto                TEXT NOT NULL,
descripcion         TEXT NOT NULL,
creado_por          INTEGER REFERENCES roomy.usuarios(id) NOT NULL,
fecha_creacion      TIMESTAMP NOT NULL,
fecha_actualizacion TIMESTAMP NOT NULL,
votos               INTEGER

);


/*8 talve este no */
CREATE TABLE roomy.feed (
  
id                  SERIAL PRIMARY KEY,
descripcion         TEXT NOT NULL,
foto                TEXT NOT NULL,
creado_por          INTEGER REFERENCES roomy.usuarios(id) NOT NULL,
fecha_creacion       TIMESTAMP NOT NULL,
tipo                INTEGER REFERENCES roomy.roles(id_rol) NOT NULL

);


/*8*/
CREATE TABLE roomy.metricas (
  


);
