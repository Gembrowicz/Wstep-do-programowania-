print("Zawartość pliku przed dopisaniem:\n")

with open("notowania_gieldowe.txt", "r") as plik:
    for linia in plik:
        print(linia.strip())

# Dopisanie nowej spółki
with open("notowania_gieldowe.txt", "a") as plik:
    plik.write("\nALR, 113")

print("\nZawartość pliku po dopisaniu:\n")

with open("notowania_gieldowe.txt", "r") as plik:
    for linia in plik:
        print(linia.strip())