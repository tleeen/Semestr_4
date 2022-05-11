CREATE TABLE chair
(id	NUMBER(3),
name	VARCHAR2(100)
CONSTRAINT name_chair_nn NOT NULL,
phone VARCHAR2(30),
CONSTRAINT dept_id_pk PRIMARY KEY (id));
