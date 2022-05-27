CREATE TABLE Kinds_sportsman
(id     NUMBER(3),
Kind_of_sport_id       NUMBER(3),
CONSTRAINT Kinds_sport_id_pk PRIMARY KEY (id),
CONSTRAINT Kinds_Kind_id_fk FOREIGN KEY(Kind_of_sport_id) REFERENCES Kind_of_sport(id));