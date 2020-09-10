CREATE TABLE efgraph(
    pic_id SERIAL PRIMARY KEY,
    grafica BYTEA,
);

CREATE TABLE public.lectura
(
    lectura_id SERIAL PRIMARY KEY,
    valor_pot_digt numeric (16,8),
    rev_min numeric (16,8),
    dif_01 numeric (16,8),
    voltaje numeric (16,8),
    dif_23 numeric (16,8),
    voltajein numeric(16,8),
    tiemp numeric (16,8)
    
    
);

CREATE TABLE reporte (
reporte_id SERIAL PRIMARY KEY,
	nombre CHARACTER VARYING(60),
	fecha CHARACTER VARYING(60),
	archivo BYTEA
);
