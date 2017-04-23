#------------------------------------------------------------
#        Script MySQL.
#------------------------------------------------------------

#------------------------------------------------------------
#		 Dropping tables.
#------------------------------------------------------------

DROP TABLE IF EXISTS Cours;
DROP TABLE IF EXISTS Utilisateur;
DROP TABLE IF EXISTS Groupe;
DROP TABLE IF EXISTS Etudiant;
DROP TABLE IF EXISTS Promotion;
DROP TABLE IF EXISTS Fiche;
DROP TABLE IF EXISTS enseigne;
DROP TABLE IF EXISTS contient;
DROP TABLE IF EXISTS appartient;

#------------------------------------------------------------
# Table: Cours
#------------------------------------------------------------

CREATE TABLE Cours(
        IDCours       int (11) Auto_increment  NOT NULL ,
        IntituleCours Varchar (25) ,
        DebutCours    Datetime ,
        FinCours      Datetime ,
        PRIMARY KEY (IDCours )
)ENGINE=InnoDB;


#------------------------------------------------------------
# Table: Utilisateur
#------------------------------------------------------------

CREATE TABLE Utilisateur(
        idUtil          int (11) Auto_increment  NOT NULL ,
        first_name  Varchar (25) ,
        last_name   Varchar (25) ,
        password    Varchar (50) ,
        email       Varchar (25) ,
        username    Varchar (25) ,
        isSuperuser Boolean ,
        TraceNFC    Varchar (25) ,
        ValidationKey Varchar (100),
        Validated Integer,
	isScanning Integer,
	hasBadged Integer,
        PRIMARY KEY (idUtil )
)ENGINE=InnoDB;


#------------------------------------------------------------
# Table: Groupe
#------------------------------------------------------------

CREATE TABLE Groupe(
        IDGroupe       int (11) Auto_increment  NOT NULL ,
        IntituleGroupe Varchar (25) ,
	IDPromo int(11),
        PRIMARY KEY (IDGroupe )
)ENGINE=InnoDB;


#------------------------------------------------------------
# Table: Etudiant
#------------------------------------------------------------

CREATE TABLE Etudiant(
        IDEtud     int (11) Auto_increment  NOT NULL ,
        NomEtud    Varchar (25) ,
        PrenomEtud Varchar (25) ,
        MailEtud   Varchar (25) ,
        hasBadged  Boolean ,
        TraceNFC   Varchar (25) ,
        IDPromo    Int ,
        PRIMARY KEY (IDEtud )
)ENGINE=InnoDB;


#------------------------------------------------------------
# Table: Promotion
#------------------------------------------------------------

CREATE TABLE Promotion(
        IDPromo       int (11) Auto_increment  NOT NULL ,
        IntitulePromo Varchar (25) ,
        PRIMARY KEY (IDPromo )
)ENGINE=InnoDB;


#------------------------------------------------------------
# Table: Fiche
#------------------------------------------------------------

CREATE TABLE Fiche(
        IDFiche int (11) Auto_increment  NOT NULL ,
        Valide  Boolean ,
        PRIMARY KEY (IDFiche )
)ENGINE=InnoDB;


#------------------------------------------------------------
# Table: enseigne
#------------------------------------------------------------

CREATE TABLE enseigne(
        NomSalle Varchar (25) ,
        IDCours  Int NOT NULL ,
        idUtil       Int NOT NULL ,
        IDFiche  Int NOT NULL ,
        PRIMARY KEY (IDCours ,idUtil ,IDFiche )
)ENGINE=InnoDB;


#------------------------------------------------------------
# Table: contient
#------------------------------------------------------------

CREATE TABLE contient(
        IDFiche Int NOT NULL ,
        IDEtud  Int NOT NULL ,
        PRIMARY KEY (IDFiche ,IDEtud )
)ENGINE=InnoDB;


#------------------------------------------------------------
# Table: appartient
#------------------------------------------------------------

CREATE TABLE appartient(
        IDGroupe Int NOT NULL ,
        IDEtud   Int NOT NULL ,
        PRIMARY KEY (IDGroupe ,IDEtud )
)ENGINE=InnoDB;


#------------------------------------------------------------
# Table: a_groupe
#------------------------------------------------------------

CREATE TABLE a_groupe(
        IDGroupe Int NOT NULL ,
        IDCours  Int NOT NULL ,
        PRIMARY KEY (IDGroupe ,IDCours )
)ENGINE=InnoDB;

ALTER TABLE Groupe
ADD CONSTRAINT fk_promo_id FOREIGN KEY (IDPromo) REFERENCES Promotion(IDPromo);

ALTER TABLE a_groupe
ADD CONSTRAINT fk_group_id FOREIGN KEY (IDGroupe) REFERENCES Groupe(IDGroupe);

ALTER TABLE a_groupe
ADD CONSTRAINT fk_cours_id FOREIGN KEY (IDCours) REFERENCES Cours(IDCours);

ALTER TABLE Etudiant ADD CONSTRAINT FK_Etudiant_IDPromo FOREIGN KEY (IDPromo) REFERENCES Promotion(IDPromo);
ALTER TABLE enseigne ADD CONSTRAINT FK_enseigne_IDCours FOREIGN KEY (IDCours) REFERENCES Cours(IDCours);
ALTER TABLE enseigne ADD CONSTRAINT FK_enseigne_id FOREIGN KEY (idUtil) REFERENCES Utilisateur(idUtil);
ALTER TABLE enseigne ADD CONSTRAINT FK_enseigne_IDFiche FOREIGN KEY (IDFiche) REFERENCES Fiche(IDFiche);
ALTER TABLE contient ADD CONSTRAINT FK_contient_IDFiche FOREIGN KEY (IDFiche) REFERENCES Fiche(IDFiche);
ALTER TABLE contient ADD CONSTRAINT FK_contient_IDEtud FOREIGN KEY (IDEtud) REFERENCES Etudiant(IDEtud);
ALTER TABLE appartient ADD CONSTRAINT FK_appartient_IDGroupe FOREIGN KEY (IDGroupe) REFERENCES Groupe(IDGroupe);
ALTER TABLE appartient ADD CONSTRAINT FK_appartient_IDEtud FOREIGN KEY (IDEtud) REFERENCES Etudiant(IDEtud);

INSERT INTO `Promotion` (`IDPromo`, `IntitulePromo`) VALUES
(1, 'M1 ILC'),
(2, 'M1 ISI'),
(3, 'ENSIIE');

INSERT INTO `Groupe` (`IDGroupe`, `IntituleGroupe`) VALUES
(1, 'Groupe 1 Compilation'),
(2, 'Groupe 1 Anglais'),
(3, 'Groupe CM Compilation'),
(4, 'Groupe 1 Algo Dist');


INSERT INTO `Fiche` (`IDFiche`, `Valide`) VALUES
(1, true),
(2, false),
(3, true),
(4, false),
(5, false);



INSERT INTO `Etudiant` (`IDEtud`, `NomEtud`, `PrenomEtud`, `MailEtud`, `hasBadged`, `TraceNFC`, `IDPromo`) VALUES
(1, 'Faraux', 'Sylvein', 'sylvein.faraux@gmail.com', false, "FFFFF", 1),
(2, 'Haegelin', 'Marc', 'marc.haegelin@gmail.com',false, "FFFFF", 1),
(3, 'Sagayaradjou', 'Davy', 'davy.sagayaradjou@gmail.c',false, "FFFFF",1),
(4, 'Nom1', 'Prenom1', 'prenom1.nom1@gmail.com',false, "FFFFF", 2),
(5, 'Nom2', 'Prenom2', 'prenom2.nom2@gmail.com',false, "FFFFF", 2),
(6, 'Nom3', 'Prenom3', 'prenom3.nom3@gmail.com',false, "FFFFF", 2),
(7, 'Nom4', 'Prenom4', 'prenom4.nom4@gmail.com',false, "FFFFF", 3),
(8, 'Nom5', 'Prenom5', 'prenom5.nom5@gmail.com',false, "FFFFF", 3),
(9, 'Nom6', 'Prenom6', 'prenom6.nom6@gmail.com',false, "FFFFF", 3),
(10, 'Nom7', 'Prenom7', 'prenom7.nom7@gmail.com',false, "FFFFF", 3),
(11, 'Nom8', 'Prenom8', 'prenom8.nom8@gmail.com',false, "FFFFF", 3),
(12, 'Nom9', 'Prenom9', 'prenom9.nom9@gmail.com',false, "FFFFF", 3),
(13, 'Nom10', 'Prenom10', 'prenom10.nom10@gmail.com', false, "FFFFF",3),
(14, 'Nom11', 'Prenom11', 'prenom11.nom11@gmail.com',false, "FFFFF", 3),
(15, 'Nom12', 'Prenom12', 'prenom12.nom12@gmail.com',false, "FFFFF", 3),
(16, 'Nom13', 'Prenom13', 'prenom13.nom13@gmail.com', false, "FFFFF",3),
(17, 'Nom14', 'Prenom14', 'prenom14.nom14@gmail.com', false, "FFFFF",3);




INSERT INTO `Cours` (`IDCours`, `IntituleCours`, `DebutCours`, `FinCours`) VALUES
(1, 'CM Compilation', '2016-12-12 08:30:00', '2016-12-12 10:30:00'),
(2, 'TD Compilation Groupe 1', '2016-12-12 10:30:00', '2016-12-12 12:30:00'),
(3, 'Anglais Groupe 1', '2016-12-12 13:30:00', '2016-12-12 15:30:00'),
(4, 'CM Algo Dist', '2016-12-13 08:30:00', '2016-12-13 10:30:00'),
(5, 'TP Algo Dist Groupe 1', '2016-12-13 10:30:00', '2016-12-13 12:30:00');


INSERT INTO `Utilisateur` (`idUtil`, `first_name`, `last_name`, `password`, `email`, `username`, `isSuperuser`, `TraceNFC`) VALUES
(1, 'Cedric', 'Bastoul', '0b9c2625dc21ef05f6ad4ddf47c5f203837aa32c', 'email', 'cb', false, 'EFZTREF'),
(2, 'Philippe', 'Clauss', 'toto', `email`, `username`, false, 'EFZTREF'),
(3, 'Frank', 'McKenna', 'toto', `email`, `username`, false, 'EFZTREF'),
(4, 'Stella', 'Marc', 'toto', `email`, `username`, false, 'EFZTREF'),
(5, 'Christian', 'Ronce', 'toto', `email`, `username`, false, 'EFZTREF');


INSERT INTO `contient` (`IDFiche`, `IDEtud`) VALUES
(1, 1),
(2, 1),
(2, 2),
(2, 3),
(3, 1),
(4, 1),
(5, 1),
(5, 2),
(5, 3);


INSERT INTO `appartient` (`IDGroupe`, `IDEtud`) VALUES
(1, 17),
(1, 16),
(2, 10),
(2, 11),
(2, 12),
(3, 1),
(4, 1),
(4, 2),
(4, 3);



INSERT INTO `enseigne` (`NomSalle`, `IDCours`, `idUtil`, `IDFiche`) VALUES
('A301', 1, 2 , 1),
('J5', 2, 1, 2),
('CLR', 3, 3, 3),
('A301', 4, 4, 4),
('J4', 5, 4, 5);

