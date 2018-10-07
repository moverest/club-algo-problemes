# Trouver son chemin entre deux articles sur Wikipédia

T’es-tu déjà perdu sur Wikipédia au point de tomber sur un sujet totalement différent de celui sur lequel tu es parti en cliquant simplement sur les liens dans les articles (_e.g._ en partant d’un article sur la banane, on tombe sur la philosophie)? Si c’est le cas, bienvenue dans le club, pour les autre, c’est le moment de commencer. Et pour ça, rien de mieux qu’un petit programme.

## Le but

Le but de ce problème est de trouver la suite de lien à cliquer pour passer d’un article à un autre. Par exemple, en partant de l’article sur la banane, on peut parcourir: Cultivar, Carl von Linnée, Naturaliste, XIXe siècle, Mikhaïl Bakounine, pour tomber sur la philosophie.

Il faudra donc écrire un programme qui trouve un chemin en donnant le nom des articles intermédiaires.

Pour t’aider, l’URL d’un article est de la forme `https://fr.wikipedia.org/wiki/{nom de l’article}`. Il faudra donc se restreindre à ce type d’URL.

# Bonus
Pour améliorer le programme, on pourra dans un second temps:

- Ne parcourir un article qu’une fois
- Chercher le plus court chemin
- Ne pas parcourir les liens entre parenthèses. Par exemple dans l’article sur la philosophie, on trouve au début: “(composé de φιλεῖν, philein : « aimer » ; et de σοφία, sophia : « sagesse » ou « savoir »)”. “Sagesse” ne sera pas pris en compte.
