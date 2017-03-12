from django.conf.urls import url
from django.views.generic.base import TemplateView
from . import views

urlpatterns = [
    url(r'^$', views.EcranLogin, name='login'),
    url(r'^accueil/$', views.accueil, name='accueil'),
    #url(r'^accueil/addutil$', views.addutil, name='addutil'),
    #url(r'^logout$', views.log_out, name='logout'),
    url(r'^Fiche$', views.fiche, name='fiche'),
	#url(r'^Validated$', views.validated, name='validated'),
	url(r'^Test$', views.test, name='test'),
    url(r'^signup/$', views.signup, name='signup'),
    url(r'^accueil/ajaxetud$', views.ajaxetud, name='ajaxetud'),
    url(r'^accueil/ajaxutil$', views.ajaxutil, name='ajaxutil'),
    url(r'^trace$', views.trace, name='traceNFC'),
]
