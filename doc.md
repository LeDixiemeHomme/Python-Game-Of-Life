# Game of Life #

## Documentation ##

### Repository ###

Cloner le projet : https://github.com/LeDixiemeHomme/Python-Game-Of-Life

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

L'affichage est géré par pygame et tkinter, une fenetre s'ouvre au lancement pour recolter des paramtres grace a tkinter puis le jeu se lance avec pygame.

Les données du tableau sont affichés a l'aide de rafraichissement de la page.

Puis a la fin on peut fermer la page du jeu et rejouer si on le désire.

Les paramètres sont testés et si une valeur est inappropriée on lance le jeu avec des paramètres par defaut.
 
 
### Répartition du travail par les contributors ###

Benoît Valle (LeDixiemeHomme) s'est chargé de mettre en place toutes les fenetre d'affichage, ainsi que de rendre le projet executable et disponible via PyPI.
 
Simon Halimi (Simonpo95) s'est chargé de mettre en place tous le fonctionnement back end de l'application, de la mise en place des éléments dans le tableau à leur comportement tout au long du jeu.
 
### Installation ###

Deux méthodes :
    
    I Passer par pypi : 
    
    pip install Vallegameoflife==1.0.9
    
    Puis lancer avec la commande "Vallegameoflife"
 

    II Cloner le repository :
    
    git clone https://github.com/LeDixiemeHomme/Python-Game-Of-Life
    
    Se mettre à la racine, executer la commande "python setup.py develop" pour installer la projet.
    
    Ensuite on peut lancer le projet grâce a la commande " Vallegameoflife ".