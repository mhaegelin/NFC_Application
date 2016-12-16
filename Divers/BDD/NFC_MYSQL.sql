#------------------------------------------------------------
#        Script MySQL.
#------------------------------------------------------------

--
-- Table structure for table `auth_user`
--

CREATE TABLE IF NOT EXISTS `auth_user` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `password` varchar(128) NOT NULL,
  `last_login` datetime DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(30) NOT NULL,
  `last_name` varchar(30) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=5 ;

--
-- Dumping data for table `auth_user`
--

INSERT INTO `auth_user` (`id`, `password`, `last_login`, `is_superuser`, `username`, `first_name`, `last_name`, `email`, `is_staff`, `is_active`, `date_joined`) VALUES
(1, 'pbkdf2_sha256$30000$mpJk3ZEpyN3j$5ebMmT+rr+dRg7SBLFiH3KxaabofDeB4os9bFW0q1AE=', '2016-12-11 14:11:12', 1, 'asususer', '', '', 'asususer@gmail.com', 1, 1, '2016-11-20 14:27:40');

#------------------------------------------------------------
# Table: Cours
#------------------------------------------------------------

CREATE TABLE Cours(
        IDCours       int (11) Auto_increment  NOT NULL ,
        IntituleCours Varchar (25) ,
        DebutCours    Datetime ,
        FinCours      Datetime ,
        IDGroupe      Int ,
        PRIMARY KEY (IDCours )
)ENGINE=InnoDB;


#------------------------------------------------------------
# Table: Utilisateur
#------------------------------------------------------------

CREATE TABLE Utilisateur(
        id          int (11) Auto_increment  NOT NULL ,
        first_name  Varchar (25) ,
        last_name   Varchar (25) ,
        password    Varchar (25) ,
        email       Varchar (25) ,
        username    Varchar (25) ,
        isSuperuser Bool ,
        TraceNFC    Varchar (25) ,
        PRIMARY KEY (id )
)ENGINE=InnoDB;


#------------------------------------------------------------
# Table: Groupe
#------------------------------------------------------------

CREATE TABLE Groupe(
        IDGroupe       int (11) Auto_increment  NOT NULL ,
        IntituleGroupe Varchar (25) ,
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
        hasBadged  Bool ,
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
        Valide  Bool ,
        PRIMARY KEY (IDFiche )
)ENGINE=InnoDB;


#------------------------------------------------------------
# Table: enseigne
#------------------------------------------------------------

CREATE TABLE enseigne(
        NomSalle Varchar (25) ,
        IDCours  Int NOT NULL ,
        id       Int NOT NULL ,
        IDFiche  Int NOT NULL ,
        PRIMARY KEY (IDCours ,id ,IDFiche )
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

ALTER TABLE Cours ADD CONSTRAINT FK_Cours_IDGroupe FOREIGN KEY (IDGroupe) REFERENCES Groupe(IDGroupe);
ALTER TABLE Etudiant ADD CONSTRAINT FK_Etudiant_IDPromo FOREIGN KEY (IDPromo) REFERENCES Promotion(IDPromo);
ALTER TABLE enseigne ADD CONSTRAINT FK_enseigne_IDCours FOREIGN KEY (IDCours) REFERENCES Cours(IDCours);
ALTER TABLE enseigne ADD CONSTRAINT FK_enseigne_id FOREIGN KEY (id) REFERENCES Utilisateur(id);
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

INSERT INTO `Etudiant` (`IDEtud`, `NomEtud`, `PrenomEtud`, `MailEtud`, `hasBadged`, `TraceNFC`, `IDPromo`) VALUES
(1, 'Faraux', 'Sylvein', 'sylvein.faraux@gmail.com', false, "FFFFF", 1),
(2, 'Heagelin', 'Marc', 'marc.haegelin@gmail.com',false, "FFFFF", 1),
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
