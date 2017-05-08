#------------------------------------------------------------
#        Script MySQL.
#------------------------------------------------------------


#-------Declaration evenement--------------------------------

SET GLOBAL event_scheduler = 1;


CREATE EVENT RESET_MORNING
    ON SCHEDULE EVERY 1 DAY 
	STARTS CURRENT_DATE + INTERVAL 1 DAY + INTERVAL 6 HOUR
    DO UPDATE Etudiant SET hasBadged = 0;

CREATE EVENT RESET_AFTERNOON
    ON SCHEDULE EVERY 1 DAY 
	STARTS CURRENT_DATE + INTERVAL 1 DAY + INTERVAL 13 HOUR
    DO UPDATE Etudiant SET hasBadged = 0;
	
CREATE EVENT RESET_MORNING_USER
    ON SCHEDULE EVERY 1 DAY 
	STARTS CURRENT_DATE + INTERVAL 1 DAY + INTERVAL 6 HOUR
    DO UPDATE Utilisateur SET hasBadged = 0;

CREATE EVENT RESET_AFTERNOON_USER
    ON SCHEDULE EVERY 1 DAY 
	STARTS CURRENT_DATE + INTERVAL 1 DAY + INTERVAL 13 HOUR
    DO UPDATE Utilisateur SET hasBadged = 0;


#------------------------------------------------------------



INSERT INTO `Promotion` (`IDPromo`, `IntitulePromo`) VALUES
(1, 'M1 ILC'),
(2, 'M1 ISI'),
(3, 'ENSIIE');

INSERT INTO `Groupe` (`IDGroupe`, `IntituleGroupe`, `IDPromo`) VALUES
(1, 'Groupe 1 Compilation', 1),
(2, 'Groupe 1 Anglais', 1),
(3, 'Groupe CM Compilation', 3),
(4, 'Groupe 1 Algo Dist', 1);


INSERT INTO `Fiche` (`IDFiche`, `Valide`) VALUES
(1, false),
(2, false),
(3, false),
(4, false),
(5, false);


INSERT INTO `Etudiant` (`IDEtud`, `NomEtud`, `PrenomEtud`, `MailEtud`, `hasBadged`, `TraceNFC`, `IDPromo`) VALUES
(1, 'Faraux', 'Sylvein', 'sylvein.faraux@gmail.com', false, "FFIJIERG", 1),
(2, 'Haegelin', 'Marc', 'marc.haegelin@gmail.com',false, "AED16796", 1),
(3, 'Sagayaradjou', 'Davy', 'davy.sagayaradjou@gmail.c',true, "FFFFF",1),
(4, 'Martin', 'Paul', 'prenom1.nom1@gmail.com',false, "FFFFF", 2),
(5, 'Marcel', 'Meline', 'prenom2.nom2@gmail.com',false, "FFFFF", 2),
(6, 'Baner', 'Bruce', 'prenom3.nom3@gmail.com',false, "FFFFF", 2),
(7, 'Toral', 'Claude', 'prenom4.nom4@gmail.com',false, "FFFFF", 3),
(8, 'Carter', 'James', 'prenom5.nom5@gmail.com',false, "FFFFF", 3),
(9, 'Tarotte', 'Eric', 'prenom6.nom6@gmail.com',false, "FFFFF", 3),
(10, 'Eluard', 'Paul', 'prenom7.nom7@gmail.com',false, "FFFFF", 3),
(11, 'Picasse', 'Pablo', 'prenom8.nom8@gmail.com',false, "FFFFF", 3),
(12, 'Wilson', 'Maxime', 'prenom9.nom9@gmail.com',false, "FFFFF", 3),
(13, 'Grasse', 'Dany', 'prenom10.nom10@gmail.com', false, "FFFFF",3),
(14, 'Sarl', 'Remy', 'prenom11.nom11@gmail.com',false, "FFFFF", 3),
(15, 'Karl', 'Lucie', 'prenom12.nom12@gmail.com',false, "FFFFF", 3),
(16, 'Idri', 'Sandrine', 'prenom13.nom13@gmail.com', false, "FFFFF",3),
(17, 'Perez', 'Caroline', 'prenom14.nom14@gmail.com', false, "FFFFF",3);


INSERT INTO `Cours` (`IDCours`, `IntituleCours`, `DebutCours`, `FinCours`) VALUES
(1, 'CM Compilation', '2017-05-09 00:00:00', '2017-05-09 17:30:00'),
(2, 'TD Compilation Groupe 1', '2017-05-10 08:30:00', '2017-05-10 10:30:00'),
(3, 'Anglais Groupe 1', '2017-05-10 13:30:00', '2017-05-10 15:30:00'),
(4, 'CM Algo Dist', '2017-05-10 15:30:00', '2017-05-10 17:30:00'),
(5, 'TP Algo Dist Groupe 1', '2017-05-11 10:30:00', '2017-05-11 12:30:00');


INSERT INTO `Utilisateur` (`idUtil`, `first_name`, `last_name`, `password`, `email`, `username`, `isSuperuser`, `isScanning`, `TraceNFC`, `ValidationKey`, `Validated`) VALUES
(1, 'Cedric', 'Bastoul', '0b9c2625dc21ef05f6ad4ddf47c5f203837aa32c', 'email', 'cb', false, false, 'EFZTREF', 'randomValidationKey', false),
(2, 'Philippe', 'Clauss', '0b9c2625dc21ef05f6ad4ddf47c5f203837aa32c', `email`, 'pc', false, false, 'EFZTREF', 'randomValidationKey', true),
(3, 'Frank', 'McKenna', 'toto', `email`, `username`, false, false, 'EFZTREF', 'randomValidationKey', false),
(4, 'Stella', 'Marc', 'toto', `email`, `username`, false, false, 'EFZTREF', 'randomValidationKey', false),
(5, 'Christian', 'Ronce', 'toto', `email`, `username`, false, false, 'EFZTREF', 'randomValidationKey', false),
(6, 'Admin', 'Admin', '0b9c2625dc21ef05f6ad4ddf47c5f203837aa32c', 'email', 'Admin', true, false, 'EFZTREF', 'randomValidationKey', false);


INSERT INTO `contient` (`IDFiche`, `IDEtud`) VALUES
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
(3, 2),
(3, 3),
(3, 10);


INSERT INTO `a_groupe` (`id`, `IDCours`, `IDGroupe`) VALUES
(1, 1, 3),
(4, 3, 3),
(2, 5, 1),
(3, 2, 1),
(5, 4, 1),
(6, 4, 2);

INSERT INTO `enseigne` (`NomSalle`, `IDCours`, `idUtil`, `IDFiche`) VALUES
('A301', 1, 2 , 1),
('J5', 2, 1, 2),
('CLR', 3, 3, 3),
('A301', 4, 4, 4),
('J4', 5, 4, 5);

