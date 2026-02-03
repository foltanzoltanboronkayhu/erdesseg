import random
import os
import sys
import datetime

#Globális változók
sizes = []
mert = []
mertsorba = []
nominal_size = 20500            # mikrométerben
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

def meretgen():
    ''' mérési eredmények generálása (mintaszam darab)'''
    mi = 0
    x = 0
    global akt_size
    akt_size = nominal_size
    global max_size
    global min_size
    max_size = 20510                # mikrométerben
    min_size = 20480                # mikrométerben
    while mi < mintaszam:
        x = random.randint(randmin, randmax)
        if akt_size + x >= min_size and akt_size + x <= max_size:
            akt_size = akt_size + x
            sizes.append(akt_size)
            mi = mi + 1

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
    kozepvonal =  max(mert)-((max(mert) - min(mert))/2)

def raszamol():
    #Átlagos érdesség számolás
    m = 0
    su = 0
    global ra
    while m < alaphossz-1:
        su = su + abs(mert[m]-kozepvonal)
        m = m + 1
        ra = f"{(su/alaphossz):.3f}"

def rzszamol():
    #Egyenetlenség magasság számolása
    global rz
    max5 = mertsorba[len(mertsorba)-1]+mertsorba[len(mertsorba)-2]+mertsorba[len(mertsorba)-3]+mertsorba[len(mertsorba)-4]+mertsorba[len(mertsorba)-5]
    min5 = mertsorba[0]+mertsorba[1]+mertsorba[2]+mertsorba[3]+mertsorba[4]
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
    print("A megengedett legnagyobb méret       : " + str(max_size) + " [um]")
    print("Az alaphosszon mért legnagyobb méret : " + str(max(mert)) + " [um]")
    print("A megengedett legkisebb méret        : " + str(min_size) + " [um]")
    print("Az alaphosszon mért legkisebb méret  : " + str(min(mert)) + " [um]")
    print("Középvonal méret                     : " + str(kozepvonal) + "[um]") 
    print("Az átlagos érdesség               Ra : " + str(ra) + "[um]")
    print("Az egyenetlenség magasság         Rz : " + str(rz) + "[um]")
    print("Histogram '1 csillag = 1 előfordulás'")
    for i in range(max_size-min_size):
        count = mertsorba.count(min_size+i)
        print(str(min_size+i) + " [um]", count * "*")
    print("~~~~~~~~~~~~~~~~~~~~~~~~")   
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
    print("A megengedett legnagyobb méret       : " + str(max_size) + " [um]")
    prYellow("Az alaphosszon mért legnagyobb méret: " + str(max(mert)) + " [um]")
    print("A megengedett legkisebb méret        : " + str(min_size) + " [um]")
    prYellow("Az alaphosszon mért legkisebb méret : " + str(min(mert)) + " [um]")
    print("Középvonal méret                     : " + str(kozepvonal) + "[um]") 
    prGreen("Az átlagos érdesség              Ra : " + str(ra) + "[um]")
    prGreen("Az egyenetlenség magasság        Rz : " + str(rz) + "[um]")
    print("Histogram '1 csillag = 1 előfordulás'")
    for i in range(max_size-min_size):
        count = mertsorba.count(min_size+i)
        print(str(min_size+i) + " [um]", count * "*")
    print("~~~~~~~~~~~~~~~~~~~~~~~~")

meretgen()
mergen()
mertsorbagen()
sorbamertsorba()
kozepszamol()
raszamol()
rzszamol()
kiirfileba()
kiirat()