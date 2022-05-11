drop VIEW EMP_VU;
drop VIEW CHA_VU;
drop index index_lec;
drop sequence chair_ID_SEQ;
drop sequence lecturer_ID_SEQ;
@@ drop chair
@@ drop lecturer
@@ cha
@@ lec
@@ chair_ID_SEQ
@@ lecturer_ID_SEQ
@@i_cha 'UNESCO CHAIR IN INFORMATION COMPUTING TECHNOLOGIES' '8 (3842) 58-23-10'
@@i_lec 'Zakharov' 'Yuri' 'Doctor of Physical and Mathematical Sciences' 'Professor' '01-09-96' 6
@@i_lec 'Stepanov' 'Yuri' 'Doctor of Technical Sciences' 'Professor' '02-03-96' 6
@@i_cha 'DEPARTMENT OF FUNDAMENTAL AND APPLIED CHEMISTRY' '8 (9039) 46-70-13'
@@i_lec 'Luzgarev' 'Sergey' 'PhD in Chemistry' 'Assistant professor' '01-03-99' 7
@@i_lec 'Ramazanova' 'Galina' 'PhD in Chemistry' 'Assistant professor' '23-04-96' 7
@@i_cha 'DEPARTMENT OF APPLIED MATHEMATICS' '8 (3842) 58-37-43'
@@i_lec 'Krutikov' 'Vladimir' 'Doctor of Technical Sciences' 'Professor' '01-07-91' 8
@@i_lec 'Gutova' 'Svetlana' 'PhD in Engineering' 'Assistant professor' '15-08-92' 8
@@i_cha 'DEPARTMENT OF FUNDAMENTAL MATHEMATICS' '8 (3842) 58-08-80'
@@i_lec 'Kucher' 'Nikolay' 'Doctor of Physical and Mathematical Sciences' 'Professor' '20-10-90' 9
@@i_lec 'Medvedev' 'Alexey' 'Doctor of Physical and Mathematical Sciences' 'Professor' '01-12-95' 9
@@i_cha 'DEPARTMENT OF GENERAL AND EXPERIMENTAL PHYSICS' '8 (3842) 58-36-95'
@@i_lec 'Shandakov' 'Sergey' 'Ph.D' 'Professor' '01-03-96' 10
@@i_lec 'Diaghilev' 'Denis' 'PhD' 'Assistant professor' '17-10-92' 10
desc chair
@@cons chair
desc lecturer
@@cons lecturer
@@index_lec
@@che_index_lec
@@che_lecturer_ID_SEQ
@@che_chair_ID_SEQ
select * from chair;
select * from lecturer;
@@view_lec
select * from EMP_VU;
@@view_cha
select * from CHA_VU;