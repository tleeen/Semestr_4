CREATE TABLE Sports_organization
(id     NUMBER(3),
title      VARCHAR2(50)
CONSTRAINT title_Sports_organization_nn NOT NULL,
address		VARCHAR2(50),
CONSTRAINT Sports_organ_id_pk PRIMARY KEY (id));