



CREATE TABLE public.payment (
	id_payment int4 NOT NULL,
	type_payment varchar(10) NULL,
	desc_payment varchar(20) NULL,
	CONSTRAINT id_payment_pk PRIMARY KEY (id_payment)
);


CREATE TABLE public.product (
	id_prod int4 NOT NULL,
	name_prod varchar(20) NULL,
	price_prod int4 NULL,
	quan_prod int4 NULL,
	CONSTRAINT producto_pk PRIMARY KEY (id_prod)
);


CREATE TABLE public.category (
	id_cate int4 NOT NULL,
	id_prod int4 NOT NULL,
	cate_cate varchar(20) NULL,
	desc_cate varchar(20) NULL,
	CONSTRAINT category_pk PRIMARY KEY (id_cate),
	CONSTRAINT category_fk FOREIGN KEY (id_prod) REFERENCES product(id_prod)
);


CREATE TABLE public.sales (
	id_sales int4 NOT NULL,
	id_prod int4 NULL,
	CONSTRAINT id_sales_pk PRIMARY KEY (id_sales),
	CONSTRAINT id_prod_fk FOREIGN KEY (id_prod) REFERENCES product(id_prod)
);


CREATE TABLE public.invoice (
	id_invoice int4 NOT NULL,
	id_sale int4 NULL,
	sale_date date NULL,
	sales_value int4 NULL,
	id_payment int4 NULL,
	CONSTRAINT id_invoice_pk PRIMARY KEY (id_invoice),
	CONSTRAINT id_payment_fk FOREIGN KEY (id_payment) REFERENCES payment(id_payment),
	CONSTRAINT id_sale_fk FOREIGN KEY (id_sale) REFERENCES sales(id_sales)
);

