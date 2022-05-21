CREATE TABLE Sports_object
(id     NUMBER(3),
title      VARCHAR2(50)
CONSTRAINT title_Sports_object_nn NOT NULL,
type        VARCHAR2(30)
CONSTRAINT type_Sports_object_nn NOT NULL,
address     VARCHAR2(50)
CONSTRAINT address_Sports_object_nn NOT NULL,
capacity      NUMBER(10),
ñoating_type        VARCHAR2(30),
CONSTRAINT Sports_object_id_pk PRIMARY KEY (id));