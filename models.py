#-*- coding: utf-8 -*-
from django.db import models
import random
import string


class MiniURL(models.Model):
    """ Définition du modèle permettant le stockage d'une URL. """
    url = models.URLField(verbose_name=u"URL à réduire", unique=True)
    code = models.CharField(max_length=6, unique=True)
    date = models.DateTimeField(auto_now_add=True, verbose_name="Date d'enregistrement")
    pseudo = models.CharField(max_length=255, blank=True, null=True)
    nb_acces = models.IntegerField(default=0, verbose_name=u"Nombre d'accès à l'URL")

    def __unicode__(self):
        """ Chaine de retour dans le cas d'un affichage de l'objet """
        return u"[{0}] {1}".format(self.code, self.url)

    def save(self, *args, **kwargs):
        """
            Surcharge de la méthode de sauvegarde, pour prendre en
            compte la génération du code
        """
        if self.pk is None:
            self.generer(6)

        super(MiniURL, self).save(*args, **kwargs)

    def generer(self, N):
        """ Génération d'un code aléatoire de N caractères """
        caracteres = string.letters + string.digits
        aleatoire = [random.choice(caracteres) for _ in xrange(N)]

        self.code = ''.join(aleatoire)

    class Meta:
        verbose_name = "Mini URL"
        verbose_name_plural = "Minis URL"
