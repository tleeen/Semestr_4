CREATE TABLE Competition
(id     NUMBER(3),
date_C      DATE
CONSTRAINT date_C_Competition_nn NOT NULL,
time_C 		VARCHAR2(7),
Sports_object_id      NUMBER(3),
Kind_of_sport_id     NUMBER(3),
Sports_category_id      NUMBER(3),
CONSTRAINT Competition_id_pk PRIMARY KEY (id),
CONSTRAINT Comp_Sports_object_id_fk FOREIGN KEY(Sports_object_id) REFERENCES Sports_object(id),
CONSTRAINT Comp_Kind_of_sport_id_fk FOREIGN KEY(Kind_of_sport_id) REFERENCES Kind_of_sport(id),
CONSTRAINT Comp_Sports_category_id_fk FOREIGN KEY(Sports_category_id) REFERENCES Sports_category(id));