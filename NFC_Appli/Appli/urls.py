from django.conf.urls import url
from django.views.generic.base import TemplateView
from . import views

urlpatterns = [
    url(r'^$', views.EcranLogin, name='login'),
    url(r'^accueil/$', views.accueil, name='accueil'),
    #url(r'^accueil/addutil$', views.addutil, name='addutil'),
    #url(r'^logout$', views.log_out, name='logout'),
    url(r'^Fiche$', views.fiche, name='fiche'),
	url(r'^Validated$', views.validated, name='validated'),
    #url(r'^signup/$', views.signup, name='signup'),
    url(r'^test/$', views.test, name='test'),
    url(r'^update_scanning/$', views.update_scanning, name='update_scanning'),
    url(r'^accueil/ajaxetud$', views.ajaxetud, name='ajaxetud'),
    url(r'^accueil/ajaxaddetud$', views.ajaxaddetud, name='ajaxaddetud'),
    url(r'^accueil/ajaxdeletud', views.ajaxdeletud, name='ajaxdeletud'),
    url(r'^accueil/ajaxchangeetud', views.ajaxchangeetud, name='ajaxchangeetud'),
    url(r'^accueil/ajaxutil$', views.ajaxutil, name='ajaxutil'),
    url(r'^accueil/changepassword$', views.changepassword, name='changepassword'),
    url(r'^accueil/ajaxlistetud$', views.ajaxlistetud, name='ajaxlistetud'),
    url(r'^accueil/ajaxlistpromo$', views.ajaxlistpromo, name='ajaxlistpromo'),
	url(r'^accueil/ajaxdelpromo$', views.ajaxdelpromo, name='ajaxdelpromo'),
	url(r'^accueil/ajaxdelgroupe$', views.ajaxdelgroupe, name='ajaxdelgroupe'),
	url(r'^accueil/ajaxaddgroupe$', views.ajaxaddgroupe, name='ajaxaddgroupe'),
	url(r'^accueil/ajaxchangegroupe$', views.ajaxchangegroupe, name='ajaxchangegroupe'),
	url(r'^accueil/ajaxchangepromo$', views.ajaxchangepromo, name='ajaxchangepromo'),
	url(r'^accueil/ajaxaddpromo$', views.ajaxaddpromo, name='ajaxaddpromo'),
    url(r'^accueil/ajaxfiche$', views.ajaxfiche, name='ajaxfiche'),
    url(r'^accueil/deleteuser$', views.deleteuser, name='deleteuser'),
    url(r'^accueil/printfiche$', views.printfiche, name='printfiche'),
	url(r'^accueil/adduser$', views.adduser, name='adduser'),
    url(r'^accueil/changeuser$', views.changeuser, name='changeuser'),
    url(r'^accueil/changefiche$', views.changefiche, name='changefiche'),
    url(r'^accueil/validateAccount$', views.validateAccount, name='validateAccount'),
    url(r'^trace$', views.trace, name='traceNFC'),
]
