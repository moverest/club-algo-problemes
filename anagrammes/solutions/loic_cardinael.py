IdLettre={'e':2,'a':3,'i':5,'s':7,'n':11,'r':13,'t':17,'o':19,'l':23,'u':29,'d':31,'c':37,'m':43,'p':47,'g':53,'b':59,'v':61,'h':67,'f':71,'q':73,'y':79,'x':83,'j':87,'k':89,'w':97,'z':101,}

def anagramme(dico):
    L={}
    for i in dico:
        s=1
        for j in i:
            s*=IdLettre[j]
        if s in L.keys():
            L[s].append(i)
        else:
            L[s]=[i]
    for i in L.values():
        if len(i)>1:
            print(i)

anagramme(['renne','danger','reine','neige','regle','reglai','aigle','gamma','enigme','arene','arena','mirage','magie','gamme','grande','magma','mygale','egale','egal','legal','legale','large','agile','maigri','maigrie','lego','glace','glacon','garcon','grele','regler','reglera','argile','argot','escargot','champignon','sanglier','foret'])
