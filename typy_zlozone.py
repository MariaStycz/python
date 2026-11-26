#listy
owoce = ["jablko", "banan", "wisnia","banan"]
print(owoce [1]) #string
print(owoce[1:2]) #rugi nawias otwarty
print(owoce[1:3])
print(owoce[1:])

owoce[2]= "truskawka"

#dozolone duplikaty

#lista jest zmienialna wiec funkcje ktore uruchamiamy nie sa do niczego przypisywane
owoce.sort()
print(owoce) #owoce to obiekt, wiec mozemy dodac funkcje

owoce.append("borowka")
print(owoce)

owoce.append(["a","b"]) #lista w liscie
owoce.extend(["a","b"]) #lista rozpakowana
print(owoce)

#macierz
owoce = [["jablko", "banan", "wisnia","banan"],
         ["jablko", "banan", "wisnia","xyz","abc"],
]

el = owoce [1][3] #[w][k]
print(el)
print(owoce[1])

owoce[0][2] = "kiwi"
print(owoce)

print(len(owoce[1]))

#lista z tekstu
tekst_CSV = "03/22/2025 jan KOWalski wyplata PLN: 8359"
moja_lista = tekst_CSV.split(" ")
moja_lista = tekst_CSV.split()
print(moja_lista)
#['03/22/2025', 'jan', 'KOWalski', 'wyplata', 'PLN:', '8359']

#moja_lista.extend(moja_lista[1]+" "+moja_lista[2])
moja_lista.append(moja_lista[1]+" "+moja_lista[2])
print(moja_lista)

moja_lista.pop(1)
moja_lista.pop(1) #elementy sie przesunely wiec teraz 2 jest 1
print(moja_lista)
#['03/22/2025', 'wyplata', 'PLN:', '8359', 'jan KOWalski']

#alternatywa
#del moja_lista[2:4]         nie wszystkie funkcje wywoluje sie kropką

#skoryguj znaki w imieniu i nazwisku
moja_lista[4] = moja_lista[4].title() #kowalski to tekst ktory jest niezmienialny wiec trzeba podmienic
print(moja_lista)

##############################
print("*" * 60)
#krotka-tuple
krotka = ("jablko", "banan", "wisnia","banan")
#krotka[0] = abc  #nie dziala
#print(krotka[0])

#rozpakowanie krotki - listy sie tak nie da
a,b,c,d = krotka
print("a",a)

##############################
#zestawy,zbiory
zbior = {"jablko", "banan", "wisnia","banan"}
print(zbior)

unikalne = list(zbior)
print(unikalne) # nie wiemy w jakiej kolejnosci beda dane w liscie utworzonej ze zbioru

##############################
#slowniki-dict
dict={
    "brand":"Ford",
    "model":"Mondeo",
    "year":2018,
    10: "abc",
    (51.1,17.0): "Wrocław", #tu jest krotka
    "wlasciwosci": ["skora","klima"] #wartosci moga byc podane jako lista
}
print(dict)

x=dict.get("model")
x=dict["model"]
print(x)

print(dict["wlasciwosci"][1])

dict["year"]=2023
dict["kolor"]="czarny"
print(dict)

print(dict.items())

#dict_items([('brand', 'Ford'), ('model', 'Mondeo'), ('year', 2023), (10, 'abc'), ((51.1, 17.0), 'Wrocław'), ('wlasciwosci', ['skora', 'klima']), ('kolor', 'czarny')])

#to jest lista krotek