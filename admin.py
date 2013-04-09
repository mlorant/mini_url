#-*- coding: utf-8 -*-
from django.contrib import admin
from models import MiniURL


class MiniURLAdmin(admin.ModelAdmin):
    """
        Définition les règles d'affichage dans l'administration. Ici
        chaque attributs de la classe a un role précis. Veuillez vous
        référez au chapitre sur l'administration si vous avez oublié
        ces rôles !
    """

    list_display = ('url', 'code', 'date', 'pseudo', 'nb_acces')
    list_filter = ('pseudo', )
    date_hierarchy = 'date'
    ordering = ('date', )
    search_fields = ('url', )


# On n'oublie pas de préciser à Django de gérer l'administration
# de notre modèle, avec la classe définie juste au dessus.
admin.site.register(MiniURL, MiniURLAdmin)
