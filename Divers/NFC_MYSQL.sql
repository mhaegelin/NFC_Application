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
























