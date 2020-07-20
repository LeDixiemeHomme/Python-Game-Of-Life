# Game of Life #

## Documentation ##

### Source ###

Gestion des événements pygame : 
https://stackoverflow.com/questions/33227825/pygame-crashes-every-time-i-click-in-the-window

Tutoriel pygame : 
https://openclassrooms.com/fr/courses/1399541-interface-graphique-pygame-pour-python/1399674-presentation-de-pygame

https://www.youtube.com/watch?v=gx4yVcJqBaI

Données sur le jeu de la vie :
https://fr.wikipedia.org/wiki/Jeu_de_la_vie

Source structure jeu de la vie :
https://fr.wikipedia.org/wiki/Jeu_de_la_vie


### Déroulement du jeu ###

En premier temps, on récupère de l'utilisateur trois paramètres qui vont permettre d'adapter la taille, le nombre de tour et la quantité de structure présente dans l'univers généré.

Une fois ces données récupérées, on génère un runner qui contient tout le contexte du jeu, et qui sera le responsable du déroulé.

Avant de lancer le jeu, et pour éviter un contexte instable et fragile, on va dispatcher volontairement et aléatoirement dans la grid des structures aléatoires (stables, vaisseaux, oscillateurs). Ces dernières seront les éléments suffisants pour la création d'un monde en mouvement et donc intéressant pour le jeu.

Ensuite, à chaque tour, on vérifie des cellules vivantes et mortes les voisines, afin de savoir si oui, ou non, à la toute fin du tour, on doit en changer le status.

On pousse dans une list les cellules à update, pour le faire seulement à la fin du tour.

Ensuite, on passe au tour suivant, et ce jusqu'à la fin des rounds.

### Affichage ###

