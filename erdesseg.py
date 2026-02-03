import random
import os

sizes = []
mert = []
mertsorba = []
nominal_size = 20500            # mikrométerben
akt_size = nominal_size
max_size = 20510                # mikrométerben
min_size = 20480                # mikrométerben
randmin = -3                    # mikrométerben
randmax = 3                     # mikrométerben
mintaszam = 1000                # a mérési eredmények száma db 0-999
mi = 0
ho = 0
x = 0
honan = 10                      # első mérési eredmény az alaphosszon
alaphossz = 100                 # a mérések számossága az alaphosszon
# mérési eredmények generálása (mintaszam darab)
while mi < mintaszam:
    x = random.randint(randmin, randmax)
    if akt_size + x >= min_size and akt_size + x <= max_size:
        akt_size = akt_size + x
        sizes.append(akt_size)
        mi = mi + 1
# az alaphosszon mért méretek kiválasztása
while ho < alaphossz:
    mert.append(sizes[ho+honan])
    ho = ho + 1
# átpakolás mertsorba listába
i = 0
while i < alaphossz:
    mertsorba.append(mert[i])
    i =i + 1
#print(mertsorba)
# az alaphosszon mért méretek növekvő sorba rendezése
i = 0
j = 0

for i in range(len(mertsorba)-1):
    for j in range(i+1, len(mertsorba)):
        #print(i, j, mertsorba, end='')
        if mertsorba[i] > mertsorba [j]:
            mertsorba[i], mertsorba[j] = mertsorba[j], mertsorba[i]

def prBlue(skk): print("\033[34m {}\033[00m" .format(skk))
def prRed(skk): print("\033[91m {}\033[00m" .format(skk))
def prGreen(skk): print("\033[92m {}\033[00m" .format(skk))
def prYellow(skk): print("\033[93m {}\033[00m" .format(skk))
def prLightPurple(skk): print("\033[94m {}\033[00m" .format(skk))
def prPurple(skk): print("\033[95m {}\033[00m" .format(skk))
def prCyan(skk): print("\033[96m {}\033[00m" .format(skk))
def prLightGray(skk): print("\033[97m {}\033[00m" .format(skk))
def prBlack(skk): print("\033[98m {}\033[00m" .format(skk))

clear = lambda: os.system('cls')
clear()
kiir = input("Kiiratja az összes méretet? I/N : ")
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
kozepvonal =  max(mert)-((max(mert) - min(mert))/2)
print("Középvonal méret                     : " + str(kozepvonal) + "[um]")
su = 0
m = 0
while m < alaphossz-1:
    su = su + abs(mert[m]-kozepvonal)
    m = m + 1
print("Az átlagos érdesség               Ra : " + f"{(su/alaphossz):.3f}" + "[um]")

max5 = mertsorba[len(mertsorba)-1]+mertsorba[len(mertsorba)-2]+mertsorba[len(mertsorba)-3]+mertsorba[len(mertsorba)-4]+mertsorba[len(mertsorba)-5]
min5 = mertsorba[0]+mertsorba[1]+mertsorba[2]+mertsorba[3]+mertsorba[4]
print("Az egyenetlenség magasság         Rz : " + f"{((max5-min5)/5):.3}" + "[um]")

print("* * * * * * * * * *")