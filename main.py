file = open("tavok.txt","r")
lista = []
for sor in file :
    sor = sor.strip().split(" ")
    lista.append(sor)
print("1. feladat: A tavok.txt beolvasása.")


for i in lista:
    if int(i[0]) == 1 and int(i[1]) == 1:
        print(f"2. feladat: A hét első útja {i[2]} km.")
        break

fuvar = ""
nap = ""

while(True):
    nap = int(input("3. feladat: Adja meg a nap sorszámát (1-7): "))
    if nap < 8 and nap > 0:
        break
    else:
        print("Hibás adat")

while(True):
    fuvar = int(input("Adja meg a fuvar sorszámát (1-40): "))
    if(fuvar < 40 and fuvar > 0):
        break
    else:
        print("Hibás adat")

temp = 0
for i in lista:
    if int(i[0]) == nap and int(i[1]) == fuvar:
        print(f"A {nap}. nap {fuvar}. fuvarához {i[2]} km került rögzítésre.")
        temp += 1

if temp == 0:
    print("Nincs ilyen fuvar.")

dolgoz = []
for i in lista:
    if(i[0] not in dolgoz):
        dolgoz.append(i[0])
nemdolgoz = ""
for i in range(7):
    if str(i) not in dolgoz and str(i) != '0':
        nemdolgoz+= f"{str(i)} "
print(f"4. feladat: A futár nem dolgozott ezen nap(ok)on: {nemdolgoz}")


napi = [0,0,0,0,0,0,0]
gyujto = [0,0,0,0,0,0,0]
for i in lista:
    if int(i[0]) == 1:
        gyujto[0]+=1
        napi[0] += int(i[2])
    if int(i[0]) == 2:
        gyujto[1]+=1
        napi[1] += int(i[2])
    if int(i[0]) == 3:
        gyujto[2]+=1
        napi[2] += int(i[2])
    if int(i[0]) == 4:
        gyujto[3]+=1
        napi[3] += int(i[2])
    if int(i[0]) == 5:
        gyujto[4]+=1
        napi[4] += int(i[2])
    if int(i[0]) == 6:
        gyujto[5]+=1
        napi[5] += int(i[2])
    if int(i[0]) == 7:
        gyujto[6]+=1
        napi[6] += int(i[2])

for i in gyujto:
    if temp < i:
        temp = i
nap = 1
for i in gyujto:
    if i == temp:
        print(f"5. feladat: Ezen nap(ok)on volt a maximális számú fuvar: {nap}.")
        break
    else: nap+=1

print("6. feladat:")
nap = 1
for i in napi :
    print(f"\t{nap}. nap: {i} km")
    nap += 1

file2 = open("dijazas.txt","w",encoding="utf-8")
temp = ""
osszeg = 0
for i in lista:
    temp = f"{i[0]}. nap {i[1]}. út {int(i[2])*300} ft\n"
    osszeg += int(i[2])*300
    file2.write(temp)

print("7. feladat: Fuvarok ellenértékének meghatározása.")
print(f"8. feladat: A futár heti fizetése {osszeg} Ft.")