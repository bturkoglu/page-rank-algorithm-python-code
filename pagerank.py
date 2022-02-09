"Page rank algoritması"

def linkOku(goster=True):
    linkSozluk = {}
    siteler = set()   
    with open('linkler.txt') as f:
        for line in f:
            s, linkler =line.strip().split('=')
            s = s.strip()
            linkTuple = tuple(x.strip() for x in linkler.split(','))
            linkSozluk[s] = linkTuple
            siteler.add(s)
            for x in linkTuple:
                siteler.add(x)
                
    siteler = list(siteler)
    siteler.sort()
    
    if goster:
        print('Link Sözlük')
        for k in linkSozluk:
            print(k,'==>',linkSozluk[k])

        print('Siteler:', siteler)

    return linkSozluk, siteler

def BosMatrixYap(m):
    l = [[0 for x in range(m)] for j in range(m)]
    return l


def MatrixDoldur(goster = True):
    for k, v in linkSozluk.items():
        k_index = siteler.index(k)
        k_adet = len(v)
        for e in v:
            e_index = siteler.index(e)
            SiteMatrix[e_index][k_index] = 1/k_adet

    if goster:
        for i in range(m):
            for j in range(m):
                print(SiteMatrix[i][j], end= ' ')
            print()
            

def MatrixCarp():
    V_Yeni = []
    for i in range(m):
        top = 0
        for j in range(m):
            top = top + SiteMatrix[i][j] * V[j]
        V_Yeni.append(top)

    print('Yeni V:', V_Yeni)
    return V_Yeni

def MatrixAyniMi(a, b):
    fark = 0.001
    boy = len(a)
    for i in range(len(a)):
        if abs(a[i]-b[i]) > fark:
            return False

    return True

def V_MatrisiYap(ilkdeger):
    V = [ilkdeger for i in range(m)]
    return V
    
def SonucMatrisiBul(V, maxdongu = 100, goster = True):
    for i in range(1, maxdongu+1):
    
        if goster: print(i,'.Deneme:', end= ' ')
        
        V_Yeni = MatrixCarp()
        if MatrixAyniMi(V, V_Yeni):
            if goster: print(i,' adet döngü ile sonuca ulaşıldı.')
            break
        else:
            V = V_Yeni[:]
    else:
        print(n,' adet döngüye rağmen, sonuca ulaşılamadı !!!!')

    return V_Yeni

def Sirala(goster=True):
    Sonuc = []
    for i in range(m):
        Sonuc.append((V[i], siteler[i]))
    Sonuc.sort(reverse=True)

    if goster:
        print("SONUÇLAR")
        for i, j in Sonuc:
            print(j,' : ', i)

    return Sonuc
    
linkSozluk, siteler = linkOku()
m = len(siteler)
SiteMatrix = BosMatrixYap(m)
MatrixDoldur()

V = V_MatrisiYap(0.25)

V = SonucMatrisiBul(V, goster=False)

Sonuc = Sirala()
            
            
    
