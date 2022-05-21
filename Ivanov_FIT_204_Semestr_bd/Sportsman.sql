CREATE TABLE Sportsman
(id     NUMBER(3),
first_name      VARCHAR2(30)
CONSTRAINT first_name_Sportsman_nn NOT NULL,
last_name 		VARCHAR2(30)
CONSTRAINT last_name_Sportsman_nn NOT NULL,
patronymic     VARCHAR2(30)
CONSTRAINT patronymic_Sportsman_nn NOT NULL,
Sports_category_id      NUMBER(3),
Kinds_sportsman_id     NUMBER(3),
Trainer_staff_id      NUMBER(3),
Sports_organization_id       NUMBER(3),
CONSTRAINT Sportsman_id_pk PRIMARY KEY (id),
CONSTRAINT Sport_Sports_c_id_fk FOREIGN KEY(Sports_category_id) REFERENCES Sports_category(id),
CONSTRAINT Sport_Kinds_sport_id_fk FOREIGN KEY(Kinds_sportsman_id) REFERENCES Kinds_sportsman(id),
CONSTRAINT Sport_Trainer_staff_id_fk FOREIGN KEY(Trainer_staff_id) REFERENCES Trainer_staff(id),
CONSTRAINT Sport_Sports_organ_id_fk FOREIGN KEY(Sports_organization_id) REFERENCES Sports_organization(id));