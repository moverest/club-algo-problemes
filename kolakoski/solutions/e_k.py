import time


# cette fonction a une complexite spatiale en 0(n) et affiche tout dans le terminal
def naive(treshold):
    assert treshold < 10 ** 7
    shortsequence = [1, 2]
    longsequence = [1, 2, 2]
    longueur = 3
    indice = 2
    percentage = [1, 2]
    t = time.time()
    while longueur < treshold:
        shortsequence.append(longsequence[indice])
        longsequence += [1 if (longsequence[-1] - 1 and longsequence[-2] - 1) or
                              (shortsequence[-1] - 1 and longsequence[-1] - 1) or
                              (shortsequence[-1] - 2 and longsequence[-1] - 1) else 2] * shortsequence[-1]
        longueur += shortsequence[-1]
        if longueur <= treshold + longsequence[-1] - 1:
            percentage[longsequence[-1] - 1] += shortsequence[-1]
        indice += 1
    print("Here the list: ", longsequence)
    print("Here the time it took: ", time.time() - t)
    print("Here the length of the sequence ", longueur)
    print(percentage[0] / (percentage[0] + percentage[1]), "% of 1")
    print(percentage[1] / (percentage[0] + percentage[1]), "% of 2")


# cette fonction a une complexite spatiale en 0(2*n/3) mais affiche tout dans le terminal
def memorySaving(treshold):
    # initialisation
    shortsequence = [1, 2]
    longsequence = [1, 2, 2]
    longueur = 3
    indice = 2
    t = time.time()
    percentage = [1, 2]
    print(" ", end="")
    while longueur < treshold:
        shortsequence.append(longsequence[indice])
        """La condition de Kolakosky se reseume a ces 3 conditions pour 1, pour 2 c'est meme plus facile"""
        longsequence += [1 if (longsequence[-1] - 1 and longsequence[-2] - 1) or
                              (shortsequence[-1] - 1 and longsequence[-1] - 1) or
                              (shortsequence[-1] - 2 and longsequence[-1] - 1) else 2] * shortsequence[-1]
        longueur += shortsequence[-1]
        if longueur <= treshold + longsequence[-1] - 1:
            percentage[longsequence[-1] - 1] += shortsequence[-1]
        print(longsequence.pop(0), end=", ")
        shortsequence.pop(0)
    for el in longsequence:
        print(el, end=", ")
    print()
    print("Here the time it took: ", time.time() - t)
    print("Here the length of the sequence ", longueur)
    print(percentage[0] / (percentage[0] + percentage[1]), "% of 1")
    print(percentage[1] / (percentage[0] + percentage[1]), "% of 2")


# cette fonction a une complexite spatiale en 0(n/ln(n)) mais affiche tout dans un fichier texte
def memoryToHD(treshold, showPercent):
    """ Le principe est simple on utilise la meme precedente fonction mais a chaque fois que l'on rajoute un element
    dans shortsequence on retire le premier de longsequence et de shortsequene comme ca on a shortsequence qui reste stable
    mais longsequence qui augmente de maniere lineaire"""
    shortsequence = [1, 2]
    longsequence = [1, 2, 2]
    longueur = 3
    indice = 2
    t = time.time()
    temp = []
    percentage = [1, 2]
    with open("results.txt", "w+") as f:
        while longueur < treshold:
            shortsequence.append(longsequence[indice])
            longsequence += [1 if (longsequence[-1] - 1 and longsequence[-2] - 1) or
                                  (shortsequence[-1] - 1 and longsequence[-1] - 1) or
                                  (shortsequence[-1] - 2 and longsequence[-1] - 1) else 2] * shortsequence[-1]
            longueur += shortsequence[-1]
            if longueur <= treshold + longsequence[-1] - 1:
                percentage[longsequence[-1] - 1] += shortsequence[-1]
            if not (longueur % (treshold / 100)) and showPercent:
                print(longueur / (treshold))
            temp.append(longsequence.pop(0))
            if len(temp) >= 100:
                f.write(" ".join(str(x) for x in temp))
                temp = []
            shortsequence.pop(0)
        f.write(" ".join(str(x) for x in longsequence))
    print()
    print("Here the time it took: ", time.time() - t)
    print("Here the length of the sequence ", longueur)
    print(percentage[0] / (percentage[0] + percentage[1]), "% of 1")
    print(percentage[1] / (percentage[0] + percentage[1]), "% of 2")


def depthWithTrailing(treshold):  # explained
    lastDiagonal = [[1, 2, 2], [1, 2]]  # we directly jump to 2 we dont bother with the 1 state as it is useless
    """ its like we are there:
    1 2 2
    1 2   
    and we just need to append 1 modify that 1 to 2 and then add a 2 on line 2 and stage that change to to the dive or
    the ascencion as you like"""
    longeur = 3
    percentage = [1, 2]
    t=time.time()
    while longeur < treshold:
        lastDiagonal.append([1])  # we are initializing the first state
        lastDiagonal[-1].append(2)  # we immediately go to the second one as it is that one that interest us
        staging = [2]  # we stage the 2 but in fact it will be a one disguised for the first dive
        # first dive done as a separate case:
        lastDiagonal[-2].append(2)  # we already have thx to initialization the 1,2 couple done
        staging = [2]  # we stage the only change

        for i in range(-3, -len(lastDiagonal) - 1,
                       -1):  # we do our loop from the -3 as we already did -1 and -2 and we go to 0
            stagingNext = []
            for el in staging:
                if el == 2 and lastDiagonal[i][-1] == 2:
                    lastDiagonal[i] += [1, 1]
                    stagingNext += [1, 1]
                    if i == -len(lastDiagonal):
                        longeur += 2
                        if longeur <= treshold + 1:
                            percentage[0] += 2
                elif el == 2 and lastDiagonal[i][-1] == 1:
                    lastDiagonal[i] += [2, 2]
                    stagingNext += [2, 2]
                    if i == -len(lastDiagonal):
                        longeur += 2
                        if longeur <= treshold + 1:
                            percentage[1] += 2
                elif el == 1 and lastDiagonal[i][-1] == 2:
                    lastDiagonal[i].append(1)
                    stagingNext.append(1)
                    if i == -len(lastDiagonal):
                        longeur += 1
                        if longeur <= treshold:
                            percentage[0] += 1
                else:
                    lastDiagonal[i].append(2)
                    stagingNext.append(2)
                    if i == -len(lastDiagonal):
                        longeur += 1
                        if longeur <= treshold:
                            percentage[1] += 1
            if not i == -len(lastDiagonal):
                staging = [el for el in stagingNext]
    for e in lastDiagonal:
        print(e)
    print("Lenght reached: ", longeur)
    print("Time it took: ", time.time() - t)
    print(percentage[0] / (percentage[0] + percentage[1]), "% of 1")
    print(percentage[1] / (percentage[0] + percentage[1]), "% of 2")


def depthWithoutTrailing(treshold):
    lastDiagonal = [2, 2]
    longeur = 3
    t = time.time()
    percentage = [1, 2]
    while longeur < treshold:
        lastDiagonal.append(2)
        lastDiagonal[-2], staging = 2, [2]
        for i in range(-3, -len(lastDiagonal) - 1, -1):
            stagingNext = []
            for el in staging:
                if el - 1 and lastDiagonal[i] - 1:
                    lastDiagonal[i] = 1
                    stagingNext += [1, 1]
                    if not i + len(lastDiagonal):
                        longeur += 2
                        if longeur <= treshold + 1:
                            percentage[0] += 2
                elif el - 1 and lastDiagonal[i] - 2:
                    lastDiagonal[i] = 2
                    stagingNext += [2, 2]
                    if not i + len(lastDiagonal):
                        longeur += 2
                        if longeur <= treshold + 1:
                            percentage[1] += 2
                elif el - 2 and lastDiagonal[i] - 1:
                    lastDiagonal[i] = 1
                    stagingNext.append(1)
                    if not i + len(lastDiagonal):
                        longeur += 1
                        if longeur <= treshold:
                            percentage[0] += 1
                else:
                    lastDiagonal[i] = 2
                    stagingNext.append(2)
                    if not i + len(lastDiagonal):
                        longeur += 1
                        if longeur <= treshold:
                            percentage[1] += 1
            if i + len(lastDiagonal):
                staging = [el for el in stagingNext]
    print("Final state only: ", lastDiagonal)
    print("Lenght reached: ", longeur)
    print("Time it took: ", time.time() - t)
    print(percentage[0] / (percentage[0] + percentage[1]), "% of 1")
    print(percentage[1] / (percentage[0] + percentage[1]), "% of 2")


def depthWithoutTrailingCompressed(t):
    ti = time.time()
    l, le, p = [2, 2], 3, [1, 2]
    while le < t:
        l.append(2)
        l[-2], s, w = 2, [2], len(l)
        for i in range(-3, -w - 1, -1):
            sn = []
            for el in s:
                l[i] = 1 if l[i] - 1 else 2
                if not i + w:
                    le += 2 if el - 1 else 1
                    if le <= t + el - 1:
                        p[l[i] - 1] += 2 if el - 1 else 1
                sn += [l[i]] * el
            if i + w:
                s = [el for el in sn]
    print("Final state only: ", l)
    print("Lenght reached: ", le)
    print("Time it took: ", time.time() - ti)
    print(p[0] / (p[0] + p[1]), "% of 1")
    print(p[1] / (p[0] + p[1]), "% of 2")


if __name__ == "__main__":
    treshold = 10 ** 3
    print("Naive Method")
    naive(treshold)
    print()
    print("Memory Saving by only keeping the second sequence but writing the whole sequence in the terminal")
    memorySaving(treshold)
    print()
    print("Memory Saving by only keeping the second sequence but writing the whole sequence in a file")
    memoryToHD(treshold, False)
    print()
    print("Depth method but saving all the state of every 'lecture'")
    depthWithTrailing(treshold)
    print()
    print("Depth Method but saving only the last state of each 'lecture'")
    depthWithoutTrailing(treshold)
    print()
    print("Depth Method just slightly compressed function, does the same than the previous one")
    depthWithoutTrailingCompressed(treshold)
