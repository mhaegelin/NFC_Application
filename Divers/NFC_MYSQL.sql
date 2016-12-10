#------------------------------------------------------------
#        Script MySQL.
#------------------------------------------------------------



#------------------------------------------------------------
# Table: Utilisateur
#------------------------------------------------------------

CREATE TABLE Utilisateur(
        IDUtil     int (11) Auto_increment  NOT NULL ,
        NomUtil    Varchar (25) NOT NULL ,
        PrenomUtil Varchar (25) NOT NULL ,
        MDPUtil    Varchar (25) NOT NULL ,
        MailUtil   Varchar (25) NOT NULL ,
        PRIMARY KEY (IDUtil )
)ENGINE=InnoDB;


#------------------------------------------------------------
# Table: Etudiant
#------------------------------------------------------------

CREATE TABLE Etudiant(
        IDEtud     int (11) Auto_increment  NOT NULL ,
        NomEtud    Varchar (25) NOT NULL ,
        PrenomEtud Varchar (25) NOT NULL ,
        MailEtud   Varchar (25) NOT NULL ,
        IDGroupe   Int NOT NULL ,
        IDPromo    Int NOT NULL ,
        PRIMARY KEY (IDEtud )
)ENGINE=InnoDB;


#------------------------------------------------------------
# Table: Cours
#------------------------------------------------------------

CREATE TABLE Cours(
        IDCours       int (11) Auto_increment  NOT NULL ,
        IntituleCours Varchar (25) NOT NULL ,
        DebutCours    Datetime NOT NULL ,
        FinCours      Datetime NOT NULL ,
        IDSalle       Int NOT NULL ,
        PRIMARY KEY (IDCours )
)ENGINE=InnoDB;


#------------------------------------------------------------
# Table: Groupe
#------------------------------------------------------------

CREATE TABLE Groupe(
        IDGroupe       int (11) Auto_increment  NOT NULL ,
        IntituleGroupe Varchar (25) NOT NULL ,
        PRIMARY KEY (IDGroupe )
)ENGINE=InnoDB;


#------------------------------------------------------------
# Table: Salle
#------------------------------------------------------------

CREATE TABLE Salle(
        IDSalle  int (11) Auto_increment  NOT NULL ,
        NomSalle Varchar (25) ,
        PRIMARY KEY (IDSalle )
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
# Table: enseigne
#------------------------------------------------------------

CREATE TABLE enseigne(
        IDCours  Int NOT NULL ,
        IDUtil   Int NOT NULL ,
        IDGroupe Int NOT NULL ,
        PRIMARY KEY (IDCours ,IDUtil ,IDGroupe )
)ENGINE=InnoDB;

ALTER TABLE Etudiant ADD CONSTRAINT FK_Etudiant_IDGroupe FOREIGN KEY (IDGroupe) REFERENCES Groupe(IDGroupe);
ALTER TABLE Etudiant ADD CONSTRAINT FK_Etudiant_IDPromo FOREIGN KEY (IDPromo) REFERENCES Promotion(IDPromo);
ALTER TABLE Cours ADD CONSTRAINT FK_Cours_IDSalle FOREIGN KEY (IDSalle) REFERENCES Salle(IDSalle);
ALTER TABLE enseigne ADD CONSTRAINT FK_enseigne_IDCours FOREIGN KEY (IDCours) REFERENCES Cours(IDCours);
ALTER TABLE enseigne ADD CONSTRAINT FK_enseigne_IDUtil FOREIGN KEY (IDUtil) REFERENCES Utilisateur(IDUtil);
ALTER TABLE enseigne ADD CONSTRAINT FK_enseigne_IDGroupe FOREIGN KEY (IDGroupe) REFERENCES Groupe(IDGroupe);








#------------------------------------------------------------
#INSTANCES
#------------------------------------------------------------








# Instances Utilisateur
# INSERT INTO Utilisateur VALUES (IDUtil, NomUtil, PrenomUtil, MDPUtil, MailUtil);

INSERT INTO Utilisateur VALUES (1, 'Bastoul', 'Cedric', 'toto', 'cedric.bastoul@gmail.com');
INSERT INTO Utilisateur VALUES (2, 'Clauss', 'Philippe', 'toto', 'philippe.clauss@gmail.com');
INSERT INTO Utilisateur VALUES (3, 'McKenna', 'Frank', 'toto', 'frank.mckenna@gmail.com');
INSERT INTO Utilisateur VALUES (4, 'Marc-Zwecker', 'Stella', 'toto', 'stella.marc-zwecker@gmail.com');
INSERT INTO Utilisateur VALUES (5, 'Fournaise', 'Myriam', 'toto', 'myriam.fournaise@gmail.com');
INSERT INTO Utilisateur VALUES (6, 'Testeur', 'Pro', 'toto', 'testeur.pro@gmail.com');




# Instances Groupe
# INSERT INTO Groupe VALUES (IDGroupe, IntituleGroupe);

INSERT INTO Groupe VALUES (1, 'Groupe 1 Compilation');
INSERT INTO Groupe VALUES (2, 'Groupe 1 Anglais');
INSERT INTO Groupe VALUES (3, 'Groupe CM Compilation');
INSERT INTO Groupe VALUES (4, 'Groupe 1 Algo Dist');




# Instances Salle
# INSERT INTO Salle VALUES (IDSalle, NomSalle);

INSERT INTO Salle VALUES (1, 'A301');
INSERT INTO Salle VALUES (2, 'J0A');
INSERT INTO Salle VALUES (3, 'J4');
INSERT INTO Salle VALUES (4, 'CRL');


# Instances Promotion
# INSERT INTO Promotion VALUES (IDPromo, IntitulePromo);

INSERT INTO Promotion VALUES (1, 'M1 ILC');
INSERT INTO Promotion VALUES (2, 'M1 ISI');
INSERT INTO Promotion VALUES (3, 'ENSIIE');




# Instances Etudiant
# INSERT INTO Etudiant VALUES (IDEtud, NomEtud, PrenomEtud, MailEtud, IDGroupe, IDPromo);

INSERT INTO Etudiant VALUES (1, 'Faraux', 'Sylvein', 'sylvein.faraux@gmail.com', 1, 1);
INSERT INTO Etudiant VALUES (2, 'Heagelin', 'Marc', 'marc.haegelin@gmail.com', 1, 1);
INSERT INTO Etudiant VALUES (3, 'Sagayaradjou', 'Davy', 'davy.sagayaradjou@gmail.com', 1, 1);
INSERT INTO Etudiant VALUES (4, 'Nom1', 'Prenom1', 'prenom1.nom1@gmail.com', 1, 2);
INSERT INTO Etudiant VALUES (5, 'Nom2', 'Prenom2', 'prenom2.nom2@gmail.com', 1, 2);
INSERT INTO Etudiant VALUES (6, 'Nom3', 'Prenom3', 'prenom3.nom3@gmail.com', 1, 2);
INSERT INTO Etudiant VALUES (7, 'Nom4', 'Prenom4', 'prenom4.nom4@gmail.com', 1, 3);
INSERT INTO Etudiant VALUES (8, 'Nom5', 'Prenom5', 'prenom5.nom5@gmail.com', 1, 3);
INSERT INTO Etudiant VALUES (9, 'Nom6', 'Prenom6', 'prenom6.nom6@gmail.com', 1, 3);
INSERT INTO Etudiant VALUES (10, 'Nom7', 'Prenom7', 'prenom7.nom7@gmail.com', 1, 3);
INSERT INTO Etudiant VALUES (11, 'Nom8', 'Prenom8', 'prenom8.nom8@gmail.com', 1, 3);
INSERT INTO Etudiant VALUES (12, 'Nom9', 'Prenom9', 'prenom9.nom9@gmail.com', 1, 3);
INSERT INTO Etudiant VALUES (13, 'Nom10', 'Prenom10', 'prenom10.nom10@gmail.com', 1, 3);
INSERT INTO Etudiant VALUES (14, 'Nom11', 'Prenom11', 'prenom11.nom11@gmail.com', 1, 3);
INSERT INTO Etudiant VALUES (15, 'Nom12', 'Prenom12', 'prenom12.nom12@gmail.com', 3, 3);
INSERT INTO Etudiant VALUES (16, 'Nom13', 'Prenom13', 'prenom13.nom13@gmail.com', 3, 3);
INSERT INTO Etudiant VALUES (17, 'Nom14', 'Prenom14', 'prenom14.nom14@gmail.com', 3, 3);





# Instances Cours
# INSERT INTO Cours VALUES (IDCours, IntituleCours, DebutCours, FinCours, IDSalle);

INSERT INTO Cours VALUES (1, 'CM Compilation', '2016-12-12 08:30:00', '2016-12-12 10:30:00', 1);
INSERT INTO Cours VALUES (2, 'TD Compilation Groupe 1', '2016-12-12 10:30:00', '2016-12-12 12:30:00', 2);
INSERT INTO Cours VALUES (3, 'Anglais Groupe 1', '2016-12-12 13:30:00', '2016-12-12 15:30:00', 4);
INSERT INTO Cours VALUES (4, 'CM Algo Dist', '2016-12-13 08:30:00', '2016-12-13 10:30:00', 1);
INSERT INTO Cours VALUES (5, 'TP Algo Dist Groupe 1', '2016-12-13 10:30:00', '2016-12-13 12:30:00', 3);




# Instances enseigne
# INSERT INTO enseigne VALUES (IDCours, IDUtil, IDGroupe);

INSERT INTO enseigne VALUES (1, 2, 3);
INSERT INTO enseigne VALUES (2, 1, 1);
INSERT INTO enseigne VALUES (3, 3, 2);
INSERT INTO enseigne VALUES (4, 4, 4);
INSERT INTO enseigne VALUES (5, 4, 4);



