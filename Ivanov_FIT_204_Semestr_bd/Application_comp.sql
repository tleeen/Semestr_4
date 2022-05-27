CREATE TABLE Application_comp
(id     NUMBER(3),
date_A      DATE
CONSTRAINT date_A_Application_comp_nn NOT NULL,
Sportsman_id      NUMBER(3),
Competition_id       NUMBER(3),
CONSTRAINT Application_for_the_comp_id_pk PRIMARY KEY (id),
CONSTRAINT Application_comp_Sport_id_fk FOREIGN KEY(Sportsman_id) REFERENCES Sportsman(id),
CONSTRAINT Application_comp_Comp_id_fk FOREIGN KEY(Competition_id) REFERENCES Competition(id));