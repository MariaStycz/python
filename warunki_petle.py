# bloki warunkowe
kolor = "rozowy"

if kolor != "bialy":
    print("kupie")
#opcjonalne
else:
    print("nie kupie")
print("test")

if kolor == "bialy":
    print("kupie")
elif kolor == "rozowy":
    print("super")
#opcjonalne
else:
    print("nie kupie")

print("*" * 60)

kolor = "zielony"
cena = 90000
# kupie w cenie do 65k zielony lub bialy
# rozbudujemy bo te 2 warunki sa rownowazne (and), kolor (or)
if (kolor == "zielony" or kolor == "biały") and cena <= 65000:
    print("kupie")

if (kolor == "zielony" or \
    kolor == "bialy") and \
    cena <=65000:
    print("kupie")