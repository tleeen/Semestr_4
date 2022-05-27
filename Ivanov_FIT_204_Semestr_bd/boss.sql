drop sequence Application_comp_ID_SEQ;
drop sequence Competition_ID_SEQ;
drop sequence Kind_of_sport_ID_SEQ;
drop sequence Kinds_sportsman_ID_SEQ;
drop sequence Rewarding_ID_SEQ;
drop sequence Sports_category_ID_SEQ;
drop sequence Sports_object_ID_SEQ;
drop sequence Sports_organization_ID_SEQ;
drop sequence Sportsman_ID_SEQ;
drop sequence Trainer_ID_SEQ;
drop sequence Trainer_staff_ID_SEQ;
@@ drop Application_comp
@@ drop Competition
@@ drop Kind_of_sport
@@ drop Kinds_sportsman
@@ drop Rewarding
@@ drop Sports_category
@@ drop Sports_object
@@ drop Sports_organization
@@ drop Sportsman
@@ drop Trainer
@@ drop Trainer_staff
@@ Sports_organization
@@ Sports_object
@@ Kind_of_sport
@@ Kinds_sportsman
@@ Trainer
@@ Trainer_staff
@@ Sports_category
@@ Sportsman
@@ Competition
@@ Application_comp
@@ Rewarding
@@ Application_comp_ID_SEQ
@@ Competition_ID_SEQ
@@ Kind_of_sport_ID_SEQ
@@ Kinds_sportsman_ID_SEQ
@@ Rewarding_ID_SEQ
@@ Sports_category_ID_SEQ
@@ Sports_object_ID_SEQ
@@ Sports_organization_ID_SEQ
@@ Sportsman_ID_SEQ
@@ Trainer_ID_SEQ
@@ Trainer_staff_ID_SEQ
@@i_Sports_organization 'Russian Team' 'Patriotov 34'
@@i_Sports_organization 'Revansh' 'Comsomolskiy 53'
@@i_Sports_organization 'Start' 'Bazovaya 12'
@@i_Sports_organization 'Stepnie volki' 'Kosmicheskaya 10'
@@i_Sports_organization 'Bars' 'Voroshilova 23'
@@i_Sports_object 'Kuzbass' 'Manej' 'Bulvar Stroiteley 1' 20000 'Stone'
@@i_Sports_object 'Arena' 'Sport komleks' 'Gagarina 122' 3000 'Brus'
@@i_Sports_object 'Himik' 'Stadion' 'Kirova 35' 5000 'Gazon'
@@i_Sports_object 'Shahter' 'Stadion' 'Shahteroc 22' 4000 'Gazon'
@@i_Sports_object 'Lasurniy' 'Basseyn' 'Sovetskiy 71' 2000 'Kafel'
@@i_Kind_of_sport 'Basketball'
@@i_Kind_of_sport 'Plavaniye'
@@i_Kind_of_sport 'Football'
@@i_Kind_of_sport 'Voleyball'
@@i_Kind_of_sport 'Legkaya athletika'
@@i_Kinds_sportsman 200
@@i_Kinds_sportsman 201
@@i_Kinds_sportsman 202
@@i_Kinds_sportsman 203
@@i_Kinds_sportsman 204
@@i_Kinds_sportsman 200
@@i_Trainer 'Nikolay' 'Kucher' 'Alexeevich' 60 200
@@i_Trainer 'Anatoliy' 'Tokarev' 'Petrovich' 53 201
@@i_Trainer 'Yakov' 'Tolstikov' 'Grigorievich' 40 202
@@i_Trainer 'Elena' 'Tarasova' 'Nicolaevna' 30 203
@@i_Trainer 'Yana' 'Ivanova' 'Urievna' 20 204
@@i_Trainer_staff 900
@@i_Trainer_staff 901
@@i_Trainer_staff 902
@@i_Trainer_staff 903
@@i_Trainer_staff 904
@@i_Sports_category 'Master sporta'
@@i_Sports_category 'KMS'
@@i_Sports_category 'MSMK'
@@i_Sports_category 'ZMS'
@@i_Sports_category 'Perviy Vzrosliy'
@@i_Sportsman 'Petr' 'Ivanov' 'Mihailovich' 500 300 10 700
@@i_Sportsman 'Vitaliy' 'Filimonov' 'Eduardovich' 500 305 10 700
@@i_Sportsman 'Maxim' 'Vorobev' 'Vitalievich' 501 301 11 701
@@i_Sportsman 'Egor' 'Dereshev' 'Aleksandrovich' 502 302 12 702
@@i_Sportsman 'Mihail' 'Linev' 'Denisovich' 503 303 13 703
@@i_Sportsman 'Ekaterina' 'Sultanova' 'Andreevna' 504 304 14 704
@@i_Competition '25-04-2022 12:30' '12:30' 600 200 500
@@i_Competition '13-06-2022 17:00' '17:00' 601 201 501
@@i_Competition '12-07-2022 18:00' '18:00' 602 202 502
@@i_Competition '02-07-2022 14:35' '14:35' 603 203 503
@@i_Competition '27-10-2022 11:00' '11:00' 604 204 504
@@i_Application_comp '20-04-22' 800 100
@@i_Application_comp '05-06-22' 801 101
@@i_Application_comp '01-07-22' 802 102
@@i_Application_comp '20-06-22' 803 103
@@i_Application_comp '07-10-22' 804 104
column column_name format a15
@@i_Rewarding 1 800 100
@@i_Rewarding 2 801 101
@@i_Rewarding 5 802 102
@@i_Rewarding 3 803 103
@@i_Rewarding 10 804 104
desc Application_comp
@@cons Application_comp
desc Competition
@@cons Competition
desc Kind_of_sport
@@cons Kind_of_sport
desc Kinds_sportsman
@@cons Kinds_sportsman
desc Rewarding
@@cons Rewarding
desc Sports_category
@@cons Sports_category
desc Sports_object
@@cons Sports_object
desc Sports_organization
@@cons Sports_organization
desc Sportsman
@@cons Sportsman
desc Trainer
@@cons Trainer
desc Trainer_staff
@@cons Trainer_staff
select * from Application_comp;
select * from Competition;
select * from Kind_of_sport;
select * from Kinds_sportsman;
select * from Rewarding;
select * from Sports_category;
select * from Sports_object;
select * from Sports_organization;
select * from Sportsman;
select * from Trainer;
select * from Trainer_staff;
@@Select1;
@@Select2;
@@Select3;