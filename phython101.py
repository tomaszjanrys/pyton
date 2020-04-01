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
print("""
######################
##Dodawanie parametru#
######################
Parametr def nazwafunkcji(parametr): wprowadza do f argumnet 100
### wywolanie f nazwafunkcji(argument)
""");
def fparametr(num):#parametr num w prowadza do f argument
	name = "wynik"
	print(name);
	print(num + 100);
fparametr(100);#argument 100 wynik f to 200
print("####przekazanie  dwoch argumentow do parametrow x i y #####");
def dwaparametry(x,y):
	print(x + y);
dwaparametry(.3, .2);
dwaparametry(222, 333);
print("\n");
print("""### Uzycie RETURN        #####
         ### def freturn(x,y):      ###
         ###	return x * y;   ###
         ### print(freturn(44,22)); ###
         ##############################
""");
def freturn(x,y):
	return x * y;
print(freturn(44,22));
print("\n");
print("###########Potega .5 to liczba 0,5##############");
def sroot(x):
	return x ** .5;
print(sroot(64));
print("\n");
print("""###########Boolean true and false##############
### namex = "type sprawdza typ  zmiennej "; 
### bool1 = True; Uwaga True musi byc z DUZZEJ litery
### bool2 = 3 + 3 == 6;
### bool3 = False;
### bool4 = 3 +3 != 6
### print(bool1, bool2, bool3, bool4);
""");
namex = "type sprawdza typ  zmiennej ";
bool1 = True;
bool2 = 3 + 3 == 6;
bool3 = False;
bool4 = 3 +3 != 6
print(bool1, bool2, bool3, bool4);
print(type(bool1));
print(type(namex));
print("Wywolanie type -> print(type(zmiena))");
print("\n");
print("""########Bool operators#################""");
print("\n");
print("""
### x = 7 > 6;
### x1 = 6 <9;
### x2 = 7 >= 7;
### x3 = 7 <= 7;
### print(x, x1, x2, x3);
""");
x = 7 > 6;
x1 = 6 <9;
x2 = 7 >= 7;
x3 = 7 <= 7;
print(x, x1, x2, x3);
