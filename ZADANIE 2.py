x = int(input("wpisz x:"))
y = int(input("wpisz y:"))
z = int(input("wpisz z:"))
if x<=y and x<=z and y>z:
    najmniejsza = x
    if y <= z:
        srodek = y
        najwieksza = z
    else:
        srodek = z
        najwieksza = y

elif y<=x and y<=z:
    najmniejsza = y
    if x <= z:
        srodek = x
        najwieksza = z
    else:
        srodek = z
        najwieksza = x
else:
    najmniejsza = z
    if x<=y:
        srodek = x
        najwieksza = y
    else:
        srodek = y
        najwieksza = x
print(najmniejsza,srodek,najwieksza)