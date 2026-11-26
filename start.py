from datetime import datetime, date, timedelta #biblio wbudowana,nie trzbea pobierac w terminalu, tylko wywolac w kodzie

print("Czesc abc")
# import cowsay
# # cowsay.cow("Czesc")
# cowsay.dragon("Czesc")
# print (cowsay.char_names)

"""
komentarz
abc
abc
abc
"""

print("abc", "abc")
print("abc" + "abc")  # konkatenacja tekstow &

# zmienne
x = 5
y = 10
print(x + y)

z = x + y
print(z)

x = "kot"  # str
print(x)

g = None

wartość = 12  # int

a, b, c = (
    2,
    "Ala",
    5,
)  # tworz komentarze - tutaj definicja kilku wartosci w jednej linii
print(a, b, c)

z = 12.43  # float
q = 0.3  # 30%
w = True  # bool

y = 10.44
xx = round(float(y) + z, 2)
print(xx)

wakacje = "Leba"
kiedy = 15
kasa = 1234.37242734

print("na wakacje pojade", kiedy, "do miasta", wakacje)
print("na wakacje pojade", kiedy, "do miasta", wakacje, sep="-")
# alternatywa -F string
print(f"na wakcje pojade:{wakacje} do miasta {kiedy} wydam:{kasa:,.2f}")

ladna_liczba = f"{kasa:_.2f}".replace("_", " ")
print(f"Liczba:{ladna_liczba}")

a = 2**4  # potega
print(a)

len([132897478347])
print(len)
print(len(str(kasa)))  # len dziala tylko na zmiennych tekstowych

b = "hello,world!"
print(b[2:5])

imie = "maria"
poprawione_imie = imie.upper()
print(poprawione_imie)

imie.title()
print(imie)  # str sa niezmienne, trzeba przygotowac nowa zmienna

imie = imie.title()
print(imie)

# lancuch wywolan
imie = (
    imie.title().replace("a", "b").replace("b", "c")
)  # lamanie kodu ukosnikiem po spacji (ale po ukosniku nie moze byc spacji)
print(imie)

# wycinanie danych i poprawianie tekstu
tekst_CSV = "03/22/2025 jan KOWalski wyplata PLN: 8359"
tekst_CSV = "03/22/2025 marek pieKNY wyplata PLN: 10359"

rok = tekst_CSV [6:10]
mc = tekst_CSV [3:5]
dzien = tekst_CSV [0:2]
print(f"data: {rok}-{mc}-{dzien}")
spacja = tekst_CSV.find(" ")
wyplata = tekst_CSV.find(" wyplata")
osoba = tekst_CSV[11:wyplata].title()
pln = tekst_CSV.find("PLN:")
kasa = float(tekst_CSV[pln + 5 :])/4.33
print(f"{rok}-{mc}-{dzien} {osoba} {kasa:.2f}")

#IntelliSense - CTRL SPACJA
data = tekst_CSV[0:10]
data_prawidlowa = datetime.strptime(data, "%m/%d/%Y") #przetwarzanie daty na prawidlowy format zgodny z biblioteka
print(f" data prawidlowa :{data_prawidlowa.date()}")

#daty

from datetime import datetime, date, timedelta #biblio wbudowana,nie trzbea pobierac w terminalu, tylko wywolac w kodzie

teraz = datetime.now()
print(f"Teraz jest: {teraz}")
print("Teraz jest: ", teraz)

ladna_data = teraz.strftime ("%d.%m.%Y")
print(f"Teraz jest {ladna_data}")

#tworzenie konkretnej daty
urodziny = date(1995, 10, 25)
print(f"Urodziny: {urodziny}")

#arytmetyka dat
przyszlosc = teraz + timedelta(days=100)
print(f"Za 100 dni bedzie: {przyszlosc.date()}")
