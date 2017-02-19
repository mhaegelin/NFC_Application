from django.contrib import admin

from .models import Utilisateur
from .models import Etudiant
from .models import Groupe
from .models import Cours
from .models import Salle
from .models import Enseigne
from .models import Promotion



class UtilisateurAdmin(admin.ModelAdmin):
    # ...
    list_display = ('idutil', 'nomutil')




# Register your models here.

admin.site.register(Utilisateur, UtilisateurAdmin)
admin.site.register(Etudiant)
admin.site.register(Groupe)
admin.site.register(Cours)
admin.site.register(Salle)
admin.site.register(Enseigne)
admin.site.register(Promotion)




