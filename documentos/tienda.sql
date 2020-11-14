create database tienda;
use tienda;
create user 'sebastian'@'localhost' identified by 'C0l0mb142020++';
GRANT ALL PRIVILEGES ON tienda.* TO 'sebastian'@'localhost';


create table usuario(
    ident_usu integer (20) not null unique ,
    tipo_ident varchar (30),
    nom_usu varchar (50),
    dir_usu varchar (50),
    tel_usu integer (10),
    email_usu varchar (50),
    user_usu varchar(50),
    pass_usu varchar(50),
    constraint id_usu_pk primary key (ident_usu)
);

create table rol(
    id_rol int (20) not null unique auto_increment,
    ident_usu int,
    tipo_rol varchar (40),
    desc_rol varchar (50),
    constraint id_rol_pk primary key (id_rol),
    constraint id_usu_fk foreign key (ident_usu) references usuario(ident_usu)
);

create table producto(
    id_prod int (20) not null unique auto_increment,
    nom_prod varchar (20),
    precio_prod int (10),
    cant_prod int (20),
    constraint id_prod_pk primary key (id_prod)
);

create table categoria(
    id_cat int (20) not null unique auto_increment,
    id_prod int ,
    cat_cat varchar (20),
    des_cat varchar (20),
    constraint id_cat_pk primary key (id_cat) ,
    constraint id_cat_fk foreign key (id_prod) references producto (id_prod)
);

create table venta(
    id_venta int not null unique auto_increment,
    id_usu int,
    id_prod int,
    constraint id_venta_pk primary key (id_venta),
    constraint id_usuario_fk foreign key (id_usu) references usuario (ident_usu),
    constraint id_produto_fk foreign key (id_prod) references producto (id_prod)
);


create table medio_pago(
    id_pago int not null unique auto_increment,
    tipo_pago varchar (10),
    desc_medio varchar (20),
    constraint id_pago_pk primary key(id_pago)
);

create table factura(
    id_factura int not null unique auto_increment,
    id_venta int ,
    fec_venta date ,
    valor_venta int (10),
    id_pago int,
    constraint id_venta_pk primary key (id_factura),
    constraint id_venta_fk foreign key (id_venta) references venta (id_venta),
    constraint id_pago_fk foreign key (id_pago) references medio_pago (id_pago)
);
