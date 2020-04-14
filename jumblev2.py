import random
import getpass
from getpass import getpass
print("_" * 120)
print("_" * 120)
print("\t\t\t Witaj w Jumble game v.2")
print("_" * 120)
enterWord = getpass("W prowadź wyraz do jumblowni : ")
word = enterWord
correct = word
jumble = ""
while word:
    position = random.randrange(len(word))
    jumble += word[position]
    word = word[:position] + word[(position + 1):]
print("Zgadnij jakie to słowo =>", jumble)
guess = input("\n Zgaduję :")
while guess != correct and guess != "":
    print("Niestety, to nie to słowo :(")
    guess = input("\n Zgaduję kolejny raz  :")
if guess == correct:
    print("_" * 120)
    print("GRATULACJE tym słowem jest \t\t\t",correct)
    print("_" * 120)
print(input("GAME OVER" * 30))
from getpass import getpass
