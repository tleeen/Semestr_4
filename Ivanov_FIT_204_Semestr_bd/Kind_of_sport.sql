CREATE TABLE Kind_of_sport
(id     NUMBER(3),
title      VARCHAR2(50)
CONSTRAINT title_Kind_of_sport_nn NOT NULL,
CONSTRAINT Kind_of_sport_id_pk PRIMARY KEY (id));