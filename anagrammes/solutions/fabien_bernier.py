Dico = open("liste_mots.txt").read().split("\n")

Anagrammes = {}
for mot in Dico :
    L = [0]*256
    for c in mot :
        L[ord(c)] += 1
    # Python ne peut hasher les listes mais peut le faire sur les tuples.
    # Ici, le tuple est hashé implicitement.
    T = tuple(L)
    if T in Anagrammes : Anagrammes[T].append(mot)
    else : Anagrammes[T] = [mot]

for h in Anagrammes :
    if len(Anagrammes[h]) > 1 :
        s = ""
        for mot in Anagrammes[h] :
            s += " | "+mot
        print(s)
