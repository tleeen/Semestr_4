CREATE TABLE lecturer
(id		NUMBER(7),
last_name	VARCHAR2(20)
CONSTRAINT last_name_lecturer_nn NOT NULL,
first_name 		VARCHAR2(20),
scient_degree 		VARCHAR2(100),
academ_status       VARCHAR2(100),
start_date          DATE
CONSTRAINT start_date_lecturer_nn NOT NULL,
char_id        NUMBER(3),
CONSTRAINT emp_id_pk PRIMARY KEY (id),
CONSTRAINT lecturer_char_id_fk FOREIGN KEY(char_id) REFERENCES chair(id));