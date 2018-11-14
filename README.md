# Forritun-Skilaverkefni

# SQL Kóði

create database 2507002960_skraning;
use 2507002960_skraning;
create table Namskeid(
namskeid_id int(11) primary key,
afangaheiti varchar(128)
);
create table notendur(
notandi_id int(11) primary key,
nafn varchar(128)
);
create table skradir(
notandi_id int(11),
namskeid_id int(11),
CONSTRAINT FKnotandi_id 
  FOREIGN KEY (notandi_id) REFERENCES notendur (notandi_id),
CONSTRAINT FKnamskeid_id 
  FOREIGN KEY (namskeid_id) REFERENCES namskeid (namskeid_id)
);

insert into Namskeid
(namskeid_id, afangaheiti)
values
(1,"FORR1FG05AU"),
(2,"FORR2FA05BU"),
(3,"FORR2HF05CU"),
(4,"KEST1TR05AU"),
(5,"KEST1TR05BU"),
(6,"KEST2TR05CU");

insert into notendur(notandi_id, nafn)
values
(1,"Abdelaziz Ghazal"),
(5,"Anna Sigurðardóttir"),
(7,"Björn Jónsson"),
(6,"Emil Gautur Emilsson"),
(10,"Geir Sigurðsson"),
(11,"Gunnar Þórunnarsson"),
(4,"Kári Konráðsson"),
(14,"Kári Gunnarsson"),
(8,"Kjartan Konráðsson"),
(12,"Konráð Guðmundsson"),
(13,"Ólafur Guðmundsson"),
(9,"Ólafur Konráðsson"),
(3,"Rósa Ólafsdóttir"),
(2,"Sigríður Sturlaugsdóttir"),
(15,"Sigurður Rögnvaldur Ragnarsson");

insert into skradir(notandi_id, namskeid_id)
Values
(1,1),
(2,1),
(3,1),
(4,1),
(5,1),
(6,2),
(7,2),
(8,2),
(9,2),
(11,2),
(10,3),
(12,3),
(13,3),
(14,3),
(15,3);
