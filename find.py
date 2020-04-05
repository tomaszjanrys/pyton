#!bin/python3
sentence = "W czasie koronowirusa należy nie wychodzić z domu !"
print(sentence)
suma = 0 
tabelka = []
i = 1
while i < 51:
    i+=1
for x in sentence:
    if (x == "o" ):
        razem = tabelka.append(suma)
        print("Hura wykryłem litere \"o\" jest na pozycji ", suma)
    else:
        print("no", suma)
    suma = suma + 1
print("Litere o znajdziesz na pozycji =>",list(tabelka))