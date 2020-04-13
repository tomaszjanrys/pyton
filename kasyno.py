import random
import matplotlib.pyplot as plt
print("_"*100)
print("\t\t\t Rzut moneta!")
print("_"*100)
print("\n Ile razy wypadnie O or R. z 1000 prob")
print("________________________________________\n")
suma = 1 
orzel = []
reszka = []
while suma < 1000:
    x = random.randint(1,2) 
    suma = suma + 1
    if x == 1:
        orzel.append(x)
    elif x==2:
        reszka.append(x)
resultOrzel = len(orzel)
resultReszka = len(reszka)
calcuO = resultOrzel / 1000 * 100
calcuR = resultReszka / 1000 * 100
print("Orzel zostal wylosowany ",len(orzel)," razy i to jest " , calcuO ,"%", "z 1000 prob")
print("Reszka zostala wylosowna",len(reszka)," razy i to jest ", calcuR,"%","z 1000 prob")
input("Game over")