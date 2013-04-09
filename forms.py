#-*- coding: utf-8 -*-
from django import forms
from models import MiniURL


class MiniURLForm(forms.ModelForm):
    """
        Définitions des champs disponibles lors de l'ajout d'une URL.
        On utilise là encore tous les outils du framework pour se
        simplifier la vie : les champs du formulaire corresponderont
        aux types de données attendus par le modèle.
    """

    class Meta:
        model = MiniURL
        fields = ('url', 'pseudo')
