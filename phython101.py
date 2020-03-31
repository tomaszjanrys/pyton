#!/bin/python3
#Print string
print("String and thing");
print('Hello world');
print("""helo world 
this 
 multi""");
print("Tomek" + "rys");
print('\n'); #new line;
print("Natalia");
print('\n');
print("Math time :");
print(50 + 50);
print(50-60);
print(50*50);
print(50/50);
print(50 + 50 / 2);
print(50 ** 2); #exponents
print(50 % 6); 
print(50 // 6); 
 #variables i methody
print("zabawa z zmiennymi i metodami");
print("comenda => print(len(nazwa zmiennej)) => pokaze dlugosc zmiennej");
quote = "All is PYTHONEM :";
print(len(quote)); 
print("comenda => print(quote.upper()) => zmienia znaki zmiennej na duze");
print(quote.upper());
print("comenda => print(quote.lower()) => zmienia znaki zmiennej na male");
print(quote.lower());
print("comenda => print(quote.title()) => zmienia pierwsze znaki  kazdego wyrazu na duze litery ");
print(quote.title());
print('\n');
print("======================================");
name = "Noob";
age = 1;
koma = 3.3;
print("zmienna age=1 => print(int(age)) => wyswietli liczbe przypisyna do zmiennej");
print(int(age));
print("printt(int(28.55)) => wyswietli liczbe calakowita");
print(int(28.55));
print("Aby wyswietlic stringi i integer nalezy intr zmienic na string poprzez => str(nazwa zmiennej z integer)");
print("Moj skill w PYTHON to  : " + name + "To jest" + str(age) + "app");
print('\n');
print('\n');
age += 1
print("zmienna => age += 1 => zwieksza zmienna o 1");
print(int(age));
print("zmienna => urodziny = 10 => age += urodziny => wynik z age zwiekszony o zmienna urodziny ");
urodziny = 10;
age += urodziny;
print(age);
print('\n');
print("""================FUNCTION===========================================================================
=== funkcje zaczynamy od : def nazwafunkcji(): | nastepnie od nowego wiersza to cialo funkcji w tym przypadku to :=
===  imie = "Marek";
===  wiek = 33;
===  print("Imie :" + imie + " Wiek" + str(wiek) + ".Thank You ");
========================================================================
funkcje wywolujemy => mojafunkcja();
""");
print('\n');
def mojafunkcja():
     imie = "Marek";
     wiek = 33;
     print("Imie :" + imie.upper() + " Wiek" + str(wiek) + ".Thank You ");
mojafunkcja();
