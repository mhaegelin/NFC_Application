# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models


class Cours(models.Model):
    idcours = models.AutoField(db_column='IDCours', primary_key=True)  # Field name made lowercase.
    intitulecours = models.CharField(db_column='IntituleCours', max_length=25, blank=True, null=True)  # Field name made lowercase.
    debutcours = models.DateTimeField(db_column='DebutCours', blank=True, null=True)  # Field name made lowercase.
    fincours = models.DateTimeField(db_column='FinCours', blank=True, null=True)  # Field name made lowercase.
    idgroupe = models.ForeignKey('Groupe', models.DO_NOTHING, db_column='IDGroupe', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        db_table = 'Cours'


class Etudiant(models.Model):
    idetud = models.AutoField(db_column='IDEtud', primary_key=True)  # Field name made lowercase.
    nometud = models.CharField(db_column='NomEtud', max_length=25, blank=True, null=True)  # Field name made lowercase.
    prenometud = models.CharField(db_column='PrenomEtud', max_length=25, blank=True, null=True)  # Field name made lowercase.
    mailetud = models.CharField(db_column='MailEtud', max_length=25, blank=True, null=True)  # Field name made lowercase.
    hasbadged = models.IntegerField(db_column='hasBadged', blank=True, null=True)  # Field name made lowercase.
    tracenfc = models.CharField(db_column='TraceNFC', max_length=25, blank=True, null=True)  # Field name made lowercase.
    idpromo = models.ForeignKey('Promotion', models.DO_NOTHING, db_column='IDPromo', blank=True, null=True)  # Field name made lowercase.

    def as_json(self):
        return dict(
            input_idetud=self.idetud,
            input_prenometud=self.prenometud,
            input_nometud=self.nometud
            )

    class Meta:
        db_table = 'Etudiant'


class Fiche(models.Model):
    idfiche = models.AutoField(db_column='IDFiche', primary_key=True)  # Field name made lowercase.
    valide = models.IntegerField(db_column='Valide', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        db_table = 'Fiche'


class Groupe(models.Model):
    idgroupe = models.AutoField(db_column='IDGroupe', primary_key=True)  # Field name made lowercase.
    intitulegroupe = models.CharField(db_column='IntituleGroupe', max_length=25, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        db_table = 'Groupe'


class Promotion(models.Model):
    idpromo = models.AutoField(db_column='IDPromo', primary_key=True)  # Field name made lowercase.
    intitulepromo = models.CharField(db_column='IntitulePromo', max_length=25, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        db_table = 'Promotion'


class Utilisateur(models.Model):
    idutil = models.AutoField(db_column='idUtil', primary_key=True)  # Field name made lowercase.
    first_name = models.CharField(max_length=25, blank=True, null=True)
    last_name = models.CharField(max_length=25, blank=True, null=True)
    password = models.CharField(max_length=75, blank=True, null=True)
    email = models.CharField(max_length=25, blank=True, null=True)
    username = models.CharField(max_length=25, blank=True, null=True)
    issuperuser = models.IntegerField(db_column='isSuperuser', blank=True, null=True)  # Field name made lowercase.
    tracenfc = models.CharField(db_column='TraceNFC', max_length=25, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        db_table = 'Utilisateur'


class Appartient(models.Model):
    idgroupe = models.ForeignKey(Groupe, models.DO_NOTHING, db_column='IDGroupe')  # Field name made lowercase.
    idetud = models.ForeignKey(Etudiant, models.DO_NOTHING, db_column='IDEtud')  # Field name made lowercase.

    class Meta:
        db_table = 'appartient'
        unique_together = (('idgroupe', 'idetud'),)


class Contient(models.Model):
    idfiche = models.ForeignKey(Fiche, models.DO_NOTHING, db_column='IDFiche')  # Field name made lowercase.
    idetud = models.ForeignKey(Etudiant, models.DO_NOTHING, db_column='IDEtud')  # Field name made lowercase.

    class Meta:
        db_table = 'contient'
        unique_together = (('idfiche', 'idetud'),)


class Enseigne(models.Model):
    nomsalle = models.CharField(db_column='NomSalle', max_length=25, blank=True, null=True)  # Field name made lowercase.
    idcours = models.ForeignKey(Cours, models.DO_NOTHING, db_column='IDCours')  # Field name made lowercase.
    idutil = models.ForeignKey(Utilisateur, on_delete=models.CASCADE, db_column='idUtil')  # Field name made lowercase.
    idfiche = models.ForeignKey(Fiche, models.DO_NOTHING, db_column='IDFiche')  # Field name made lowercase.

    class Meta:
        db_table = 'enseigne'
        unique_together = (('idcours', 'idutil', 'idfiche'),)
