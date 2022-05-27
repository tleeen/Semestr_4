CREATE TABLE Rewarding
(id     NUMBER(3),
place_in_the_competition      NUMBER(3)
CONSTRAINT place_Rewarding_nn NOT NULL,
Sportsman_id 		NUMBER(3),
Competition_id     NUMBER(3),
CONSTRAINT Rewarding_id_pk PRIMARY KEY (id),
CONSTRAINT Rewarding_Sport_id_fk FOREIGN KEY(Sportsman_id) REFERENCES Sportsman(id),
CONSTRAINT Rewarding_Comp_id_fk FOREIGN KEY(Competition_id) REFERENCES Competition(id));