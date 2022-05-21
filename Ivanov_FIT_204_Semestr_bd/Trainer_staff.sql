CREATE TABLE Trainer_staff
(id     NUMBER(3),
Trainer_id      NUMBER(3),
CONSTRAINT Trainer_staff_id_pk PRIMARY KEY (id),
CONSTRAINT Trainer_Trainer_id_fk FOREIGN KEY(Trainer_id) REFERENCES Trainer(id));