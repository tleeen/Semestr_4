CREATE TABLE Sports_category
(id     NUMBER(3),
title      VARCHAR2(50)
CONSTRAINT title_Sports_c_nn NOT NULL,
CONSTRAINT Sports_category_id_pk PRIMARY KEY (id));