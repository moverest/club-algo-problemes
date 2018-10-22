# Séquence de Kolakoski

Soit la séquence séquence S de symboles (disons pour l’exemple {1, 2, 3, 4, 5}). On appelle sa lecture la séquence L qui est le compte du nombre de répétition d’un même symbole. Par exemple:

```
S = 112221134312554333
L = 2 3  2 111112 13
```

La séquence de Kolakoski est une suite de 1 et de 2 qui se lit d’elle même, c’est-à-dire que S = L.

```
S = 122112122… 
L = 12 2 112…
```

## Le but
Le but du problème est de générer cette séquence pour une longueur donnée. On commencera par un longueur de 100 000 symboles.

## Bonus
 - Une hypothèse qui n’a toujours pas été prouvée est que le nombre de 1 et de 2 est égale quand la longueur de la séquence tend vers +∞. Donner le ratio pour une longueur donnée.
 - Trouver le ratio pour une longueur de 1 000 000 000 000 (10<sup>12</sup>). Il faudra pour cela améliorer l'algorithme car l’espace en mémoire sera le point limitant. En effet, la méthode naïve pour générer la suite a une complexité en mémoire de O(n). Écrire le programme avec une meilleur complexité spatiale (il existe des algorithmes en O(ln(n)).
