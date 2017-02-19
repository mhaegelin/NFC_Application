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
    intitulecours = models.CharField(db_column='IntituleCours', max_length=25)  # Field name made lowercase.
    debutcours = models.DateTimeField(db_column='DebutCours')  # Field name made lowercase.
    fincours = models.DateTimeField(db_column='FinCours')  # Field name made lowercase.
    idsalle = models.ForeignKey('Salle', models.DO_NOTHING, db_column='IDSalle')  # Field name made lowercase.

    class Meta:
        db_table = 'Cours'


class Etudiant(models.Model):
    idetud = models.AutoField(db_column='IDEtud', primary_key=True)  # Field name made lowercase.
    nometud = models.CharField(db_column='NomEtud', max_length=25)  # Field name made lowercase.
    prenometud = models.CharField(db_column='PrenomEtud', max_length=25)  # Field name made lowercase.
    mailetud = models.CharField(db_column='MailEtud', max_length=25)  # Field name made lowercase.
    idgroupe = models.ForeignKey('Groupe', models.DO_NOTHING, db_column='IDGroupe')  # Field name made lowercase.
    idpromo = models.ForeignKey('Promotion', models.DO_NOTHING, db_column='IDPromo')  # Field name made lowercase.

    class Meta:
        db_table = 'Etudiant'


class Groupe(models.Model):
    idgroupe = models.AutoField(db_column='IDGroupe', primary_key=True)  # Field name made lowercase.
    intitulegroupe = models.CharField(db_column='IntituleGroupe', max_length=25)  # Field name made lowercase.

    class Meta:
        db_table = 'Groupe'


class Promotion(models.Model):
    idpromo = models.AutoField(db_column='IDPromo', primary_key=True)  # Field name made lowercase.
    intitulepromo = models.CharField(db_column='IntitulePromo', max_length=25, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        
        db_table = 'Promotion'


class Salle(models.Model):
    idsalle = models.AutoField(db_column='IDSalle', primary_key=True)  # Field name made lowercase.
    nomsalle = models.CharField(db_column='NomSalle', max_length=25, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        
        db_table = 'Salle'


class Utilisateur(models.Model):
    idutil = models.AutoField(db_column='IDUtil', primary_key=True)  # Field name made lowercase.
    nomutil = models.CharField(db_column='NomUtil', max_length=25)  # Field name made lowercase.
    prenomutil = models.CharField(db_column='PrenomUtil', max_length=25)  # Field name made lowercase.
    mdputil = models.CharField(db_column='MDPUtil', max_length=25)  # Field name made lowercase.
    mailutil = models.CharField(db_column='MailUtil', max_length=25)  # Field name made lowercase.

    class Meta:
        
        db_table = 'Utilisateur'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=80)

    class Meta:
        
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        
        db_table = 'django_session'


class Enseigne(models.Model):
    idcours = models.ForeignKey(Cours, models.DO_NOTHING, db_column='IDCours')  # Field name made lowercase.
    idutil = models.ForeignKey(Utilisateur, models.DO_NOTHING, db_column='IDUtil')  # Field name made lowercase.
    idgroupe = models.ForeignKey(Groupe, models.DO_NOTHING, db_column='IDGroupe')  # Field name made lowercase.

    class Meta:
        
        db_table = 'enseigne'
        unique_together = (('idcours', 'idutil', 'idgroupe'),)
