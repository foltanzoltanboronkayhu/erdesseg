import random
import os
import sys
import datetime

#Globális változók
sizes = []
mert = []
mertsorba = []
#nominal_size = 20500            # mikrométerben
# max_size = 20510                # mikrométerben
# min_size = 20480                # mikrométerben
randmin = -2                    # mikrométerben
randmax = 2                     # mikrométerben
mintaszam = 1000                # a mérési eredmények száma db 0-999
honan = 10                      # első mérési eredmény az alaphosszon
alaphossz = 100                 # a mérések számossága az alaphosszon
su = 0
# ra = 0
# rz = 0
max5 = 0
min5 = 0
# kozepvonal = 0
currdir = ""

#tintaszín generálás
def prBlue(skk): print("\033[34m {}\033[00m" .format(skk))
def prRed(skk): print("\033[91m {}\033[00m" .format(skk))
def prGreen(skk): print("\033[92m {}\033[00m" .format(skk))
def prYellow(skk): print("\033[93m {}\033[00m" .format(skk))
def prLightPurple(skk): print("\033[94m {}\033[00m" .format(skk))
def prPurple(skk): print("\033[95m {}\033[00m" .format(skk))
def prCyan(skk): print("\033[96m {}\033[00m" .format(skk))
def prLightGray(skk): print("\033[97m {}\033[00m" .format(skk))
def prBlack(skk): print("\033[98m {}\033[00m" .format(skk))

def inidir():
    currdir = os.path.dirname(os.path.abspath(__file__))
    currdir = currdir + "/"
    #print(currdir)
    if os.path.isfile(currdir + "sizeski.txt") == True:
        print("Létezik a '" + currdir + 'sizeski.txt' + "' fájl.")
    else:
        cf = open(currdir + "sizeski.txt")
        with open(currdir + 'sizeski.txt', 'w', encoding='utf-8') as celfajl:
            x = 0
            for datok in sizes:
                cf.write(str(sizes[x]) + "\n")
                # print(sizes[x])
                x = x + 1
            cf.close()
        print("A '" + currdir + 'sizeski.txt' + "' fájl létrehozva.")


def kezd():
    '''Kezdeti értékek megadása.'''
    global nominal_size
    nominal_size = 0
    filebol = input("Beolvassa fájlból a mérési eredményeket? 'I = Igen' ")
    if filebol == "I":
        # fájl megnyitása
        forrasfajl = open('./sizeski.txt')
        with open('./sizeski.txt', 'r', encoding='utf-8') as forrasfajl:
            for sor in forrasfajl:
                sizes.append(sor.strip())
        # forrásfájl bezárása
        forrasfajl.close()
        print(str(len(sizes)) + " darab mérési eredmény beolvasva fájlból.")
        if nominal_size < 5000 or nominal_size>200000:
            #while nominal_size < 1000 and nominal_size>200000:
            nominal_size = int(input("Kérem adja meg a névleges méret értékét mikrométerben (5000~200000 között):"))

def meretgen():
    ''' mérési eredmények generálása (mintaszam darab)'''  
    global akt_size 
    akt_size = nominal_size
    global max_size
    max_size = 0
    global min_size
    min_size = 0
    mi = 0
    x = 0
    forrasfajl = open('./maxsize.txt')
    with open('./maxsize.txt', 'r', encoding='utf-8') as forrasfajl:
        for sor in forrasfajl:
            max_size=(sor.strip())
            forrasfajl.close()
    #forrasfajl = open('minsize.txt')
    with open('./minsize.txt', 'r', encoding='utf-8') as forrasfajl:
        for sor in forrasfajl:
            min_size=(sor.strip())
            forrasfajl.close()
    
    if len(sizes) == 0:
        max_size = nominal_size+random.randint(int(nominal_size / 8000),int(nominal_size / 2000))                # mikrométerben
        min_size = nominal_size-random.randint(int(nominal_size / 8000),int(nominal_size / 2000))                # mikrométerben
        while mi < mintaszam:
            x = random.randint(randmin, randmax)
            if akt_size + x >= min_size and akt_size + x <= max_size:
                akt_size = akt_size + x
                sizes.append(akt_size)
                mi = mi + 1
        print(str(len(sizes)) + " darab mérési eredmény legenerálva.")
        celfajl = open('sizeski.txt')
        with open('sizeski.txt', 'w', encoding='utf-8') as celfajl:
            x = 0
            for datok in sizes:
                celfajl.write(str(sizes[x]) + "\n")
                # print(sizes[x])
                x = x + 1
            celfajl.close()
    

def mergen():
    ''' az alaphosszon mért méretek kiválasztása'''
    ho = 0
    while ho < alaphossz:
        mert.append(sizes[ho+honan])
        ho = ho + 1

def mertsorbagen():
    '''átpakolás mertsorba listába'''
    i = 0
    while i < alaphossz:
        mertsorba.append(mert[i])
        i =i + 1
    #print(mertsorba)

def sorbamertsorba():
    '''az alaphosszon mért méretek növekvő sorba rendezése'''
    j = 0
    k = 0
    for j in range(len(mertsorba)-1):
        for k in range(j+1, len(mertsorba)):
            #print(i, j, mertsorba, end='')
            if mertsorba[j] > mertsorba [k]:
                mertsorba[j], mertsorba[k] = mertsorba[k], mertsorba[j]

def kozepszamol():
    #Középvonalhelyzet számolás
    global kozepvonal
    ma = int(max(mert))
    mi = int(min(mert))
    kozepvonal =  ma-((ma-mi)/2)

def raszamol():
    #Átlagos érdesség számolás
    m = 0
    su = 0
    global ra
    while m < alaphossz-1:
        su = su + abs(float(mert[m])-kozepvonal)
        m = m + 1
        ra = f"{(su/alaphossz):.3f}"

def rzszamol():
    #Egyenetlenség magasság számolása
    global rz
    max5 = int(mertsorba[len(mertsorba)-1]+mertsorba[len(mertsorba)-2]+mertsorba[len(mertsorba)-3]+mertsorba[len(mertsorba)-4]+mertsorba[len(mertsorba)-5])
    min5 = int(mertsorba[0]+mertsorba[1]+mertsorba[2]+mertsorba[3]+mertsorba[4])
    rz = f"{((max5-min5)/5):.3}"

def kiirfileba():
    sys.stdout = open('log.txt','wt')
    print(str(datetime.datetime.now()) + "; System implementation: " + "" + str(sys.implementation))
    print()
    print("Az összes méret: ")
    print(sizes)
    print("Mért értékek száma összesen          : " + str(len(sizes)) + " [db]")
    print("Az első mért érték helye a mérésekben: " + str(honan))
    print("A mért értékek száma az alaphosszon  : " + str(len(mert)) + " [db]")
    print("A mért értékek az alaphosszon        : ")
    print(mert)
    print("A mért értékek sorbarendezve         : ")
    print(mertsorba)
    print("A névleges méret                     : " + str(nominal_size) + " [um]")
    print("A megengedett legnagyobb méret       : " + str(max_size) + " [um]")
    print("Az alaphosszon mért legnagyobb méret : " + str(max(mert)) + " [um]")
    print("A megengedett legkisebb méret        : " + str(min_size) + " [um]")
    print("Az alaphosszon mért legkisebb méret  : " + str(min(mert)) + " [um]")
    print("Középvonal méret                     : " + str(kozepvonal) + " [um]") 
    print("Az átlagos érdesség               Ra : " + str(ra) + " [um]")
    print("Az egyenetlenség magasság         Rz : " + str(rz) + " [um]")
    print("Histogram '1 csillag = 1 előfordulás'")
    for i in range(max_size-min_size):
        count = mertsorba.count(min_size+i)
        print(str(min_size+i) + " [um]", count * "*")
    print("~~~~~~~~~~~~~~~~~~~~~~~~")   
    sys.stdout = sys.__stdout__
    sys.stdout = open('maxsize.txt','wt')
    print(str(max_size))
    sys.stdout = sys.__stdout__
    sys.stdout = open('minsize.txt','wt')
    print(str(min_size))
    sys.stdout = sys.__stdout__

def kiirat():
    #Az adatok, eredmények kiiratása
    clear = lambda: os.system('cls')
    clear()
    kiir = input("Kiiratja az összes méretet?      'I' : ")
    if kiir == "I" or kiir == "i":
        clear = lambda: os.system('cls')
        clear()
        print("Az összes méret: ")
        print(sizes)
    print("Mért értékek száma összesen          : " + str(len(sizes)) + " [db]")
    print("Az első mért érték helye a mérésekben: " + str(honan))
    print("A mért értékek száma az alaphosszon  : " + str(len(mert)) + " [db]")
    print("A mért értékek az alaphosszon        : ")
    print(mert)
    print("A mért értékek sorbarendezve         : ")
    prBlue(mertsorba)
    prYellow("A névleges méret                    : " + str(nominal_size) + " [um]")
    print("A megengedett legnagyobb méret       : " + str(max_size) + " [um]")
    prYellow("Az alaphosszon mért legnagyobb méret: " + str(max(mert)) + " [um]")
    print("A megengedett legkisebb méret        : " + str(min_size) + " [um]")
    prYellow("Az alaphosszon mért legkisebb méret : " + str(min(mert)) + " [um]")
    print("Középvonal méret                     : " + str(kozepvonal) + " [um]") 
    prGreen("Az átlagos érdesség              Ra : " + str(ra) + " [um]")
    prGreen("Az egyenetlenség magasság        Rz : " + str(rz) + " [um]")
    print("Histogram '1 csillag = 1 előfordulás'")
    for i in range(max_size-min_size):
        count = mertsorba.count(min_size+i)
        if min_size + i != int(kozepvonal):
            print(" " + str(min_size+i) + " [um]" + count * "*")
        elif min_size + i == int(kozepvonal):
            prYellow(str(min_size+i) + " [um]" + count * "*")
    print("~~~~~~~~~~~~~~~~~~~~~~~~")

inidir()
kezd()
meretgen()
mergen()
mertsorbagen()
sorbamertsorba()
kozepszamol()
raszamol()
rzszamol()
kiirfileba()
kiirat()