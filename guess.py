import random
import matplotlib.pyplot as plt
print("_"*100)
print("\t\t\t Witaj w grze 'Jaka to liczba'!")
print("_"*100)
print("\nMam na myśli pewną liczbę z zakresu od 1 do 100.")
print("Spróbuj ją odgadnąć w jak najmniejszej liczbie prób.\n")
los = random.randint(1, 100)
user = int(input("Podaj liczbe :"))
tries = 1 
triesH = 1
triesL = 1
while user != los:
    tries += 1
    if user > los:
        triesH += 1
        print("Twoja liczba jest za duza")
        user = int(input("Ta liczba to:"))
    elif user < los:
        triesL += 1
        print("Twoja liczba jest zamała")
        user = int(input("Ta liczba to:"))
    else:
       print("HURA  TRAFILES OD RAZU \n ZAGRAJ W LOTTO :)")
print("Potrzebowales na to tyle prob  ", tries)
print("Tyle razy trafiales wyzej niz liczba wygrywajaca", triesH)
print("Tyle razy trafiales nizej niz liczba wygrywajaca", triesL)
plt.hist(triesH)
plt.hist(tries)
plt.hist(triesL)
plt.show()
print(input("\n\n GAME OVER"))