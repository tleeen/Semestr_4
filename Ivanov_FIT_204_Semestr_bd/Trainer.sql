CREATE TABLE Trainer
(id     NUMBER(3),
first_name      VARCHAR2(30)
CONSTRAINT first_name_Trainer_nn NOT NULL,
last_name 		VARCHAR2(30)
CONSTRAINT last_name_Trainer_nn NOT NULL,
patronymic     VARCHAR2(30)
CONSTRAINT patronymic_Trainer_nn NOT NULL,
work_experience     NUMBER(2),
Kind_of_sport_id      NUMBER(3),
CONSTRAINT Trainer_id_pk PRIMARY KEY (id),
CONSTRAINT Trainer_sport_id_fk FOREIGN KEY(Kind_of_sport_id) REFERENCES Kind_of_sport(id));