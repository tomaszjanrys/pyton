#!bin/python3
import sys
def newline():
    print("\n")
print("____________________________________________________")
print("             I M P O R T I N G / S T R I N G        ")
print("____________________________________________________")
print("----------M O D U L E------- S Y S --------------------------------------------------------------------")
print("""Moduły obiekty  to zbiór funkcji i zmiennych. Moduły instaluje się przez klauzule I M P O R T.
Moduł sys zawiera informacje dotyczące systemu jak funkcje i parametru systemu 
""")
print("______________________________________________________________________________________________________")
print("\n")
print("""

""")
print("------ T I M E------------- ")
print("""---------------------------
---  from datetime import datetime
---  print(datetime.now())
-----------------------------------
--- from datetime import datetime as czas   => AS przypisuje do dowolnej nazwy 
--- print(czas.now())  => zamiast DATETIME uzywamy wybranej nazwy np. czas
""")
print("_________RESULTS___________ ")
from datetime import datetime
print(datetime.now())
from datetime import datetime as czas
print(czas.now())
print(czas.now())
print(czas.now())
newline()
print("_________PODSTAWOWE INFO________________ ")
newline()
print("Wersja Pythona: ",sys.version,"\n", "Wersja :", sys.version_info, "\n","Wersja API", sys.api_version)
newline()
print("Executable", sys.executable)
print("sys.maxsize", sys.maxsize)
print("sys.path => Zawiera ścieżkę przeszukiwania, gdzie Python szuka modułów.", sys.path)
newline()
print("sys.platform =>", sys.platform)
print("sys.getrecursionlimit()", sys.getrecursionlimit())
print("______________________________________________________________________________________________________________")
newline()
print("___________________________________________________")
print("                  S T R I N G                     ")
print(sys.platform.upper())
print("___________________________________________________")
print("""
--- name = "Tomasz"                                         => zmienna
--- print(name.upper())                                     => zamiana na DUZE LITERY
--- print("Pierwsza litera imienia to => ", name[0])        => wypisuje z stirngu pierwszy zank
--- print("Ostatnia litera imienia to =>", name[-1])        => odejmuje od 0 -1 wiec przechodzi na koniec strigu
--- sentence = "W czasie koronowirusa należy nie wychodzić z domu !"
--- print(sentence.title())                                 => kazdy wyraz z duzej litery
--- print("Dlugosc zdania =>", sentence.__len__())          => wyswietla dlugosc 
--- print(sentence[:14])                                    => wyswietla litery do 13 znaku
--- print(sentence[-50:])                                   => wyswietla od konca do -50 znaku 
--- print(sentence[:-14])                                   => ukrywa od konca -14 znakow 
-------------------------------------------------------------------------
""")
name = "Tomasz"
print(name.upper())
print("Pierwsza litera imienia to => ", name[0])
print("Ostatnia litera imienia to =>", name[-1])
sentence = "W czasie koronowirusa należy nie wychodzić z domu !"
print(sentence.title())
print("Dlugosc zdania =>", sentence.__len__())
print(sentence[:14])
print(sentence[-50:])
print(sentence[:-14])
newline()
print("""------S P L I T (space)------AND------- 'space'J O I N ----------------------
--- z1 = sentence.split()     => zmenna przechowuje rozdzielone zdanie
--- print(sentence.split())   => wyswietla rozdzielone zdanie
--- print(z1[2],z1[4])        => wyswietla konkretne pozycje z rozdzielonego zdania
--- join = '-'.join(z1)       => laczy spowrotem rozdzielone zdanie w ' jest ' znak rozdzielajacy wyrazy   
""")
print("_______RESULTS_________________", czas.now(),"__________")
z1 = sentence.split()
print(sentence.split())
print(z1[2],z1[4])
join = '-'.join(z1)
print(join)
newline()
print("----------- using ---\"\"---- '' ----------")
print("""
sentence2 = "Powiedzialem 'ucz sie sam'"
sentence2a = "Powiedzialem \"ucz sie sam \""
print(sentence2)
print(sentence2a)
""")
print("_______RESULTS____________________")
sentence2 = "Powiedzialem 'ucz sie sam'"
sentence2a = "Powiedzialem \"ucz sie sam \""
print(sentence2)
print(sentence2a)
print("--------------------------------------")
newline()
print("-------- I N -------------")
newline()
print("""---------------------
--- print("a" in "Mama")        => IN sprawdza czy a istnieje w MAMA i zwraca boolean TRUE
--- print("b" in "tata")        => IN sprawdza czy b istnieje w TATA i zwraca boolean FALSE
--- litera = "a"                => jakas zmiena
--- wyraz = "Abra"              => druga zmiena
--- print(litera in wyraz)      => sprawdza czy zmiena litera wystepuje w zmiennej wyraz
""")
print("_______________RESULTS_____________")
print("a" in "Mama")
print("b" in "tata")
litera = "ab"
wyraz = "abra kadArba"
print(litera in wyraz)
sp = wyraz.split()
print('=>'.join(sp).upper())
print("---------------------------------------")
newline()
print("---------- R E P L A C E ----and F I N D--------------")
print("""-----------------------------------------
namet = "Tomasz Rys "                       => 
print(namet.replace("Tomasz", "Adam"))      =>REPLACE zamienia wartosci w zmiennej 
                                            podajemy orginalny elemnt ktory zostanie zastapiny drugim 
namet2 = "Natalia Hanna"
print(namet2.find("Hanna"))   => wyswietla liczbe po ktorym  znajduje sie wyraz Hanna

""")
namet2 = "Natalia Hanna"
namet = "Tomasz Rys "
print(namet.replace("Tomasz", "Adam"))
print(namet2.find("Hanna"))
newline()
print("---------- F O R M A T --------------")
print("""
---  mymovies = "The Terminator " 
---  print("Moj ulubiny film to {}".format(mymovies))   => .format() wstawia zmienna w {}
------------------------------------------------------------------------------
""")
print("____RESULTS_____and fun____________________________")
mymovies = "The Terminator "
print("Moj ulubiny film to {}".format(mymovies))
print("Wyraz {}".format(mymovies),"za czyna się po ", mymovies.find("Terminator"), "Literze")
print(mymovies.split())
print('     '.join(mymovies), czas.now(), sys.platform)
print("_________________________________________________________________________________________")
newline()
print("____Fun def____________________________")
print("""
--- def myfav(owoce, warzywa): ==> parametry 
---     fav = "Moje ulubione owoce to : {} , a warzywa to {}".format(owoce, warzywa) ==> w {} wstawiane sa parametry  
---     return fav 
--- print(myfav("Banan", "Marchewka")) ===> Argumenty stringi przekazujemy w ""  
---------------------------------------------------------------------------------------------------------------
""")
print("_________________RESULTS________________________________________________")
def myfav(owoce, warzywa):
    fav = "Moje ulubione owoce to : {} , a warzywa to {}".format(owoce, warzywa)
    return fav
print(myfav("Banan", "Marchewka"))
newline()
print("---------- D I C T I O N A R E S --------------")
print("""skladaja sie z keys i values 
------------Exaple 1--------------------------------------------
drikns = {"szalona mucha": 10,"Czarna motyka": 50,"Zielona mila": 12, "???": 120}  ===> nazwy to key liczby to values 
print(drikns)
---------------------------------------------------------------------------------------------------------------------------------
""")
print("________________________________EXAMPLE 1_______________________")

drikns = {"szalona mucha": 10,"Czarna motyka": 50,"Zielona mila": 12, "???": 120}
print(drikns)
print("_____________________________________________________________________________")
newline()
print("""____________________________EXAMPLE 2_____update____________________________________
--- pracownicy ={"Ksiegowosc":["Tomek","Marek","Aagta","Baska"], "IT":["Zbyszek", "Marcin", "Id"], "HR":["MArta", "Asia", "Agnieszka"]}
--- print("Działy w naszej firmie :",list(pracownicy))
--- pracownicy['Robotnicy'] = ["Zdzichu", "Marecel", "Tadek buła"] ===> Dodaje nowy key i values
--- print(pracownicy)
--- pracownicy.update({"Sprzedaż": ["MArzena", "Pamela"]}) ===> U P D A T E ({"key":["values"]})
--- print(pracownicy)

""")
print("________________________________EXAMPLE 2_______________________")
pracownicy ={"Ksiegowosc":["Tomek","Marek","Aagta","Baska"], "IT":["Zbyszek", "Marcin", "Id"], "HR":["MArta", "Asia", "Agnieszka"]}
print("Działy w naszej firmie :",list(pracownicy))
pracownicy['Robotnicy'] = ["Zdzichu", "Marecel", "Tadek buła"]
print(pracownicy)
pracownicy.update({"Sprzedaż": ["MArzena", "Pamela"]})
print(pracownicy)
print("___________________________________________________________________________________________________")
print("___________________________GET ___pobiera wartosci przypisane key__________________________________")
print("Cena Szalonej muchy to ",drikns.get("szalona mucha"))
print("Pracownicy z HR to ",pracownicy.get("HR"))
print("___________________________________________________________________________________________________")
newline()
print("__________________________________L I S T and DICTIONARY________________________________________________")
books = ["Dzuma", "Dziady ", "Potop"]
authors = ["OK", "Kiepska", "VIP"]
xxx = zip(books, authors)
ddd = {key: value for key, value in xxx}
print(ddd)
ddd['Filmy'] = ["Terminator"]
print(ddd,"Ma ",len(ddd),"Elementy")
print("___________________________________________________________________________________________________")