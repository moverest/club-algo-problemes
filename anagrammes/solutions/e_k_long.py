from collections import defaultdict
from sys import getsizeof
import codecs,time


def initDico(method):
    t=time.time()
    dico=defaultdict(list)
    anagrammes=set()
    with codecs.open("liste_mot.txt","r",encoding="utf8") as l:
        for el in l:
            index=computeHash(el,method)
            dico[index].append(el.rstrip())
            if len(dico[index])>1:
                anagrammes.add(index)

    with codecs.open("liste_anagrammes"+str(method)+".txt",'w+',encoding='utf8') as f:
        for idx in anagrammes:
            f.write(" ".join(dico[idx])+"\r\n")
    return "Done in {} s".format(time.time()-t)

def computeHash(dat,hashType=0):
    mot=dat.rstrip().lower() #not necessary but lets assume word could have space in them or not be normalized
    """ 
    The hashs chosen here are pretty simple, we need them non positional as we are searching for anagrams, so we will use
    the standard alphabetic order. We also need it to be able to count the occurrences of a letter and hold that value 
    in the hash, the only issue is that it will be size dependent of the word length. Here a quick example: aabbj and
    aaaaaaaaaaaaaaaaaaaaaaaaaaa, first one have 2*a, 2*b, 1*j so hash will be 2*6^0+2*6^1+1*6^9=1953137 or 
    2200000001000000000000000000000... or 22x7x1 and the second one would be 27*28^0=27 or 27000000000000000000000000...
    or r27r. 
    
    So here you notice a few limitations, first one is nice but need to be computed for each word and can be quite heavy 
    for a large word with letters at the end of the alphabet, for instance 'Zimbabwe'. Second one is fixed in space but 
    have one huge flaw, you can only have 0 to 9 letters identical. So you need the third one that correct this error
    and also make sure all unnecessary 0 are voided, but it use some markers that unfortunately take also some space as 
    letters are heavier than straight number.
    
    I will so implement both method and the argument passed to the function will determine which one will be used.
    
    There is also an oversight a lot of times made which is to forgot that french is one of the worst language of all 
    time and have a lot of letters with variation and in this case the list is about that long: é,è,à,ê... they will be
    appended at the end of the hash as a different hash.
    The first hash as it use the length of the word have a few collisions, nothing really bad but for low length words 
    it makes the whole difference unfortunately, a simple solution I implemented is that i added the length of the word
    at the beginning of the hash.
    
    Overall the second method is the best space wise but the slowest (10.3s on the test set) while the first one take 
    about 5% more space and is faster (9.5s on the test set)
    
    Ok here a simpler hash that will be implemented as hash number 3: just take all the letter of the word then sort 
    them so hash will be the same for anagrams, ofc this solutions is ok because all the words tends to be small and
    computing hash like we did with the two solutions is overkill for small words with almost no repetitions in most 
    cases.
    """

    if not hashType:
        hash=0
        hashPart=defaultdict(int) #or lambda:0
        for letter in mot:
            if ord("a")<=ord(letter)<=ord("z"):
                hash+=(len(mot)+1)**(ord(letter)-ord("a"))
            else:
                hashPart[letter]+=1
        hashPart=sorted(hashPart.items(),key=lambda letter:letter[0])
        return str(len(mot))+str(hash)+"".join([ele[0]+str(ele[1]) for ele in hashPart])
    elif hashType==1:
        hashAlphabet=[0]*26
        hashPart = defaultdict(int)
        for letter in mot:
            if ord("a") <= ord(letter) <= ord("z"):
                hashAlphabet[ord(letter)-ord('a')]+= 1
            else:
                hashPart[letter] += 1
        hashPart = sorted(hashPart.items(), key=lambda letter: letter[0])
        hash=""
        i=0
        for e in hashAlphabet:
            if e==0:
                i+=1
            else:
                if i:
                    hash+="x"+str(i)+"x"
                hash+=str(e) if e<10 else "r"+str(e)+"r"
                i=0
        return hash+"".join([ele[0]+str(ele[1]) for ele in hashPart])
    else:
        return "".join(sorted(mot))

def tests():
    words=["elephant","éléphant","rhinocéros","rhino","habitude","habhitude","starifiérait","stratifiérai","aaaaaaaaaaaaaaaaaa"]
    for el in words:
        p,m,l=computeHash(el,0),computeHash(el,1),computeHash(el,2)
        print(p,":",getsizeof(p),m,":",getsizeof(m),l,":",getsizeof(l))


def compare():
    l1=set()
    l2=set()
    with codecs.open("liste_anagrammes0.txt","r",encoding="utf8") as f1:
        l1.add(f1)
    with codecs.open("liste_anagrammes1.txt","r",encoding="utf8") as f2:
        for el in f2:
            if el not in l1:
                l2.add(el)
            else:
                l1.remove(el)
    print("Differences: ",l1,l2)
    print("In Anagrammes1 : ")
    for el in l2:
        print(el, end=" ")
        for e in el.split():
            p, m = computeHash(e, 0), computeHash(e, 1)
            print(p, ":", getsizeof(p), m, ":", getsizeof(m))
    print("In Anagrammes0 : ")
    for el in l1:
        print(el,end="")
        for e in el.split():
            p, m = computeHash(e, 0), computeHash(e, 1)
            print(p, ":", getsizeof(p), m, ":", getsizeof(m))

if __name__=="__main__":
    for i in range(3):
        print(initDico(i))
    #tests()
