liczba_punktow = int(input("Podaj liczbę punktów:"))

if liczba_punktow > 80:
    print("zaliczenie egzaminu w terminie zerowym")
elif 50< liczba_punktow < 80:
    print("mozliwosc poprawy egzaminu")
else :
    print("egzamin niezaliczony, koniecznosc poprawy")