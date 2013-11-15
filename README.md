TP raccourcisseur d'URL
=======================

Vous trouverez dans cette archive l'ensemble des fichiers composant le
TP raccourcisseur d'URL, disponible dans le cours sur Django de 
OpenClassrooms. Cette version a été commentée, afin de vous permettre 
de voir l'utilité de chaque fichier sans pour autant reparcourir le cours,
en cas de trou de mémoire ;)

Une particularité que nous avons pas abordé dans le cours est le dossier
``templates`` au sein de l'application : vous remarquerez ici que nous
avons mis un dossier templates au sein de l'application et que les vues
appellent uniquement le nom des fichiers qu'il contient (``liste.html``
au lieu de ``mini_url/liste.html``). En réalité, chaque application peut
avoir son propre dossier templates, afin de pouvoir partager le code
facilement (comme c'est le cas ici)

Informations et pré-requis
--------------------------
- Mis à jour le 9 avril 2013
- Requiert Django 1.5 ou supérieur


Modifications à apporter au projet
----------------------------------
1. Copier/Coller le dossier ``mini_url`` dans votre projet
2. Ajouter ``'mini_url'`` au tuple ``INSTALLED_APPS`` dans le ``settings.py``
3. Ajouter ``url(r'^m/', include('mini_url.urls')),`` dans les patterns du fichier ``urls.py``
4. Exécuter la commande ``python manage.py syncdb``
5. Lancer votre serveur Django et c'est prêt à l'adresse http://localhost:8000/m/



Pour rappel, le cours est disponible à l'adresse suivante : http://fr.openclassrooms.com/informatique/cours/developpez-votre-site-web-avec-le-framework-django
