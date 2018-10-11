# Approche :
Ici le problème soumis revient à chercher un chemin entre deux nodes dans un graphe orienté non pondéré. L'algorithme classique adapté pour trouver le plus court chemin est donc une recherche en largeur (cf : https://en.wikipedia.org/wiki/Shortest_path_problem).

L'appli est divisée en trois composantes afin de découpler le pb :
-Un scraper, qui récupére toutes les urls d'une page 'scrapper.py'
-Un modèle de notre problème 'problem.py'
-Un algorithme classique de recherche en largeur 'breadth_first_search.py'

### Scraper
J'ai utilisé ici un code trouvé tel quel permettant de récupérer une page sous forme de string tout en vérifiant qu'il s'agit bien de HTML/XML correct.

J'utilise ensuite BeautifulSoup pour récupérer uniquement les URLs présentes dans le texte en plusieurs étapes :

1. je récupére uniquement le contenu pricipal de la page grace à l'option find de BeautifulSoup en précisant l'id de la balise html à récupèrer : `.find(id='mw-content-text')`
2. Ensuite, je récupère toutes les URLs de la page en filtrant par type de balise (a pour les liens), tout en filtrant le résultat grace à ma fonction `filter_url` qui renvoie l'url passée en paramètre uniquement si elle contient `/wiki/` et qu'elle ne contient pas `:` (liens Fichiers et trucs inutiles)
3. Une Comprehension List permet de génèrer le retour en un seul parcours

### Problem
Ici rien de compliqué, juste une classe stockant les urls de départ et d'arrivée, et wrappant le scraper afin de renvoyer les fils du noeud courant, et de vérifier s'ils sont notre objectif.

### breadth first search
Un algorithme classique tiré de wikipédia (https://en.wikipedia.org/wiki/Breadth-first_search) et légérement modifié pour qu'il vérifie si l'on a atteint notre but sur les fils directement, au lieu d'attendre qu'il soit sous-racine du problème (cela permet de gagner beaucoup de temps et ne change, à ma connaissance, rien au résultat).

# Usage :
Pour installer les dépendances :
`pip3 install -r requirements.txt`

Pour lancer :
`python3 problem.py /wiki/Banane /wiki/coucou
`

# Améliorations  envisagées:

### Pondérer le graphe
avec un graphe pondéré, on aurait pu réduire le temps de recherche en utilisant A* ou Dijkstra.Plusieurs options sont envisageables :
- L'utilisation du traitement naturel des langues (Natural language processing) aurait potentiellement permis d'ajouter un poids en fonction de la proximité sémantique entre les candidats et l'onjectif. Cela me paraissait en revanche compliqué à mettre en oeuvre en un temps réduit. Cela sera potentiellement couteux en calcul.

-Compter le nombre de fils de chaque noeud ? il n'est pas évident de dire si un noeud avec plus de liens est plus prometteur (plus de chances, mais plus de temps de parcours ?)

### Effectuer une recherche en partant des deux extrémités
Même si le graphe est orienté (pouvoir aller de A à B ne garantit pas de pouvoir aller de B à A) on peut espèrer trouver des pages parcourues par les deux arbres, permettant éventuellement de faire un lien direct, ou simplement de relancer l'algo à partir de ce noeud commun ?
