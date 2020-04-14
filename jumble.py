import random
WORDS = ("terorysta","marchewka", "smaczne", "koronawirus", "mercedes")
word =  random.choice(WORDS)
correct = word
jumble = ""
while word:
    position = random.randrange(len(word))
    jumble += word[position]
    word = word[:position] + word[(position + 1):]
print("Witaj w grze")
print("zgadnij jakie to slowo", jumble)
guess = input("\n Twoja odpowiedz")
while guess != correct and guess != "":
    print("Niestety to nie to slowo")
    guess = input("\n Twoja odpowiedz :")
if guess == correct:
     print("Gratulacje")
print("Game over")

