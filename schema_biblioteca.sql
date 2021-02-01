create table lectores (
	lector_id serial,
	nombre character varying(40),
	apellido character varying(40),
	documento bigint,
	unique(documento),
	constraint idLec primary key(lector_id)
	);
create table libros (
	libro_id serial,
	editorial character varying(40),
	autor character varying(40),
	titulo character varying(40),
	constraint idL primary key(libro_id)
	);
create table retiros (
	retiro_id serial,
	lector_id integer,
	libro_id integer,
	constraint fId foreign key(lector_id) references lectores(lector_id) on delete cascade,	
	constraint fId2 foreign key(libro_id) references libros(libro_id) on delete cascade	
);